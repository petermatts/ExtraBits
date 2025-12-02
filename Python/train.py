from sklearn.metrics import precision_recall_fscore_support
import torch
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
from typing import Iterable


class Trainer:
    def __init__(self,
                 model: torch.nn.Module,
                 train_loader: DataLoader,
                 val_loader: DataLoader = None,
                 optimizer: torch.optim.Optimizer = None,
                 scheduler=None,
                 loss_fn=None,
                 device: torch.device | str = None,
                 num_epochs: int = 10,
                 checkpoint_path: os.PathLike = None,
                 early_stopping_patience: int = None,
                 use_amp: bool = False,
                 plot_loss: bool = True,
                 show_metrics: bool = True,
                 show_gradients: bool = False):

        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.num_epochs = num_epochs
        self.checkpoint_path = checkpoint_path
        self.early_stopping_patience = early_stopping_patience
        self.use_amp = use_amp
        self.plot_loss = plot_loss
        self.show_metrics = show_metrics
        self.show_gradients = show_gradients

        self.model.to(self.device)

        # AMP scaler
        self.scaler = torch.amp.GradScaler(device=self.device, enabled=self.use_amp)

        # Loss function(s)
        if loss_fn is None:
            self.loss_fn = [torch.nn.BCEWithLogitsLoss(), torch.nn.CrossEntropyLoss()]
        elif isinstance(loss_fn, list):
            self.loss_fn = loss_fn
        else:
            self.loss_fn = [loss_fn]

        # Live plot data
        self.train_losses = []
        self.val_losses = []

        if self.plot_loss:
            plt.ion()
            self.fig, self.ax = plt.subplots()
            self.train_line, = self.ax.plot([], [], label="Train Loss")
            # self.val_line, = self.ax.plot([], [], label="Val Loss")
            self.ax.set_xlabel("Steps")
            self.ax.set_ylabel("Loss")
            self.ax.set_title("Loss")
            self.ax.legend()

    def _save_checkpoint(self, epoch: int, best_val_loss: float):
        if self.checkpoint_path:
            torch.save({
                'epoch': epoch,
                'model_state': self.model.state_dict(),
                'optimizer_state': self.optimizer.state_dict(),
                'best_val_loss': best_val_loss
            }, self.checkpoint_path)

    def _validate(self):
        self.model.eval()
        total_loss = 0
        total_samples = 0

        num_heads = len(self.loss_fn)
        all_preds = [[] for _ in range(num_heads)]
        all_targets = [[] for _ in range(num_heads)]

        correct_preds = [0] * num_heads
        total_preds = [0] * num_heads

        with torch.no_grad():
            for inputs, targets in self.val_loader:
                inputs = inputs.to(self.device)
                if not isinstance(targets, (list, tuple)):
                    targets = [targets.to(self.device)]
                else:
                    targets = [t.to(self.device) for t in targets]

                with torch.amp.autocast(str(self.device), enabled=self.use_amp):
                    outputs = self.model(inputs)
                    if not isinstance(outputs, (list, tuple)):
                        outputs = [outputs]

                    # Preprocess targets for loss functions
                    processed_targets = []
                    for i, (lf, o, t) in enumerate(zip(self.loss_fn, outputs, targets)):
                        if isinstance(lf, torch.nn.CrossEntropyLoss):
                            if t.ndim == o.ndim:
                                t = torch.argmax(t, dim=1)
                            t = t.long()
                        processed_targets.append(t)

                    losses = [lf(o, t) for lf, o, t in zip(self.loss_fn, outputs, processed_targets)]

                loss = sum(losses)
                total_loss += loss.item() * inputs.size(0)
                total_samples += inputs.size(0)

                for i, (output, target) in enumerate(zip(outputs, processed_targets)):
                    if isinstance(self.loss_fn[i], torch.nn.BCEWithLogitsLoss):
                        probs = torch.sigmoid(output)
                        _, topki = torch.topk(probs, k=5, dim=1)  # ! 5 is hard coded

                        preds = torch.zeros_like(target, dtype=target.dtype, device=target.device).scatter_(1, topki, 1.0)

                        # preds = (torch.sigmoid(output) > 0.1).float()
                        # # Subset accuracy (strict multi-label)
                        # sample_correct = (preds == target).all(dim=1).float()  # [B]
                        # correct_preds[i] += sample_correct.sum().item()
                        # total_preds[i] += sample_correct.shape[0]

                        correct = (preds == target).sum().item()
                        total = target.numel()
                        # correct = ((preds == 1) & (target == 1)).sum().item()
                        # total = target.sum().item()
                        correct_preds[i] += correct
                        total_preds[i] += total

                    elif isinstance(self.loss_fn[i], torch.nn.CrossEntropyLoss):
                        preds = torch.argmax(output, dim=1)
                        correct = (preds == target).sum().item()
                        total = target.size(0)
                        correct_preds[i] += correct
                        total_preds[i] += total

                    else:
                        preds = output  # fallback

                    all_preds[i].append(preds.cpu())
                    all_targets[i].append(target.cpu())

        avg_loss = total_loss / total_samples

        # Metrics
        if self.show_metrics:
            for i in range(num_heads):
                preds = torch.cat(all_preds[i])
                targets = torch.cat(all_targets[i])

                average = 'macro' if isinstance(self.loss_fn[i], torch.nn.CrossEntropyLoss) else 'samples'
                precision, recall, f1, _ = precision_recall_fscore_support(
                    targets.numpy(), preds.numpy(), average=average, zero_division=0
                )

                # print(f"[Head {i}] Precision: {precision:.4f} | Recall: {recall:.4f} | F1: {f1:.4f}")

                if total_preds[i] > 0:
                    accuracy = correct_preds[i] / total_preds[i]
                    print(f"[Head {i}] Accuracy: {accuracy:.4f} | precision: {precision:.4f} | Recall: {recall:.4f} | F1: {f1:.4f}")

        return avg_loss, None

    def _update_plot(self):
        self.train_line.set_data(range(1, len(self.train_losses) + 1), self.train_losses)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.00001)

    def _plot_gradients_and_weights(self):
        fig, axes = plt.subplots(2, 1, figsize=(8, 6))
        axes[0].set_title("Gradient Magnitudes")
        axes[1].set_title("Weight Magnitudes")

        for name, param in self.model.named_parameters():
            if param.grad is not None:
                axes[0].hist(param.grad.detach().cpu().numpy().flatten(), bins=100, alpha=0.5, label=name)
            axes[1].hist(param.detach().cpu().numpy().flatten(), bins=100, alpha=0.5, label=name)

        for ax in axes:
            ax.legend(fontsize='small', loc='upper right')
            ax.set_yscale('log')
        plt.tight_layout()
        plt.show()

    def learn(self):  # just for funzies
        self.train()

    def train(self):
        best_val_loss = float('inf')
        patience_counter = 0

        for epoch in range(1, self.num_epochs + 1):
            self.model.train()
            running_loss = 0.0

            for inputs, targets in tqdm(self.train_loader, desc=f"Epoch {epoch}/{self.num_epochs}"):
                inputs = inputs.to(self.device)
                if not isinstance(targets, (list, tuple)):
                    targets = [targets.to(self.device)]
                else:
                    targets = [t.to(self.device) for t in targets]

                self.optimizer.zero_grad()

                with torch.amp.autocast(str(self.device), enabled=self.use_amp):
                    outputs = self.model(inputs)
                    if not isinstance(outputs, (list, tuple)):
                        outputs = [outputs]

                    losses = [lf(o, t) for lf, o, t in zip(self.loss_fn, outputs, targets)]

                loss = sum(losses)
                self.scaler.scale(loss).backward()
                self.scaler.step(self.optimizer)
                self.scaler.update()

                running_loss += loss.item() * inputs.size(0)

                if self.plot_loss:
                    self.train_losses.append(loss.detach().cpu().item())
                    self._update_plot()

            train_loss = running_loss / len(self.train_loader.dataset)
            self.train_losses.append(train_loss)
            print(f"[Epoch {epoch}] Train Loss: {train_loss:.4f}")

            if self.val_loader:
                val_loss, _ = self._validate()
                print(f"[Epoch {epoch}] Val Loss: {val_loss:.4f}")

                if self.scheduler:
                    self.scheduler.step(val_loss)

                if val_loss < best_val_loss:
                    best_val_loss = val_loss
                    patience_counter = 0
                    self._save_checkpoint(epoch, best_val_loss)
                else:
                    patience_counter += 1

                if self.early_stopping_patience and patience_counter >= self.early_stopping_patience:
                    print("Early stopping triggered.")
                    break
            else:
                self.val_losses.append(None)

            if self.plot_loss:
                self._update_plot()

        if self.plot_loss:
            plt.ioff()
            plt.show()


if __name__ == "__main__":
    # trainer = Trainer(
    #     model=my_model,
    #     train_loader=train_loader,
    #     val_loader=val_loader,
    #     optimizer=optimizer,
    #     loss_fn=[
    #         torch.nn.BCEWithLogitsLoss(),    # for head 1
    #         torch.nn.CrossEntropyLoss()      # for head 2
    #     ],
    #     num_epochs=20,
    #     checkpoint_path='checkpoint.pt',
    #     early_stopping_patience=5,
    #     use_amp=True,
    #     plot_loss=True
    # )
    pass
