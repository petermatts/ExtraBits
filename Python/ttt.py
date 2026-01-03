from enum import StrEnum
from pathlib import Path
import os
import torch
from tqdm import tqdm
# import importlib
# import colorama
# import logging

# a torch train tester for all use cases

def vprint(msg: str, verbose: bool) -> None:
    if verbose:
        print(msg)
    

def get_optimal_device(verbose: bool = False) -> torch.device:
    """
    Usage:
        device = get_optimal_device()
        model.to(device)
        tensor.to(device)
    """
    # # Try TPU (XLA) if available
    # xla_spec = importlib.util.find_spec("torch_xla.core.xla_model")
    # if xla_spec is not None:
    #     try:
    #         import torch_xla.core.xla_model as xm
    #         device = xm.xla_device()
    #         vprint("Using TPU (XLA) device.", verbose)
    #         vprint(f"    XLA device: {device}", verbose)
    #         return device
    #     except Exception as e:
    #         vprint(f"TPU detected but failed to initialize: {e}", verbose)

    # CUDA
    if torch.cuda.is_available():
        device = torch.device("cuda")
        num_devices = torch.cuda.device_count()
        vprint(f"Using CUDA. {num_devices} device(s) detected:", verbose)
        for i in range(num_devices):
            props = torch.cuda.get_device_properties(i)
            total_mem = round(props.total_memory / (1024 ** 3), 2)
            vprint(f"  [{i}] {props.name} - {total_mem} GB VRAM", verbose)

        current_id = torch.cuda.current_device()
        used_mem = round(torch.cuda.memory_allocated(current_id) / (1024 ** 2), 2)
        reserved_mem = round(torch.cuda.memory_reserved(current_id) / (1024 ** 2), 2)
        vprint(f"\tMemory usage (Device {current_id}): Allocated {used_mem} MB / Reserved {reserved_mem} MB", verbose)
        vprint(f"\tMixed Precision Support (AMP): {'Yes' if torch.cuda.is_bf16_supported() else 'No'}", verbose)
        return device #? support returning multiple devices if more than 1 detected

    # MPS (Apple Silicon)
    elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        device = torch.device("mps")
        vprint("Using Apple Metal Performance Shaders (MPS) backend.", verbose)
        vprint("\tNote: MPS does not yet support advanced memory queries in PyTorch.", verbose)
        return device

    # CPU fallback
    else:
        device = torch.device("cpu")
        vprint(f"No GPUs available. Using CPU. Device: {device}", verbose)
        return device


class Optimizers(StrEnum):
    Adadelta = 'Adadelta'
    Adafactor = 'Adafactor'
    Adagrad = 'Adagrad'
    Adam = 'Adam'
    AdamW = 'AdamW'
    SparseAdam = 'SparseAdam'
    Adamax = 'Adamax'
    ASGD = 'ASGD'
    LBFGS = 'LBFGS'
    NAdam = 'NAdam'
    RMSprop = 'RMSprop'
    Rprop = 'Rprop'
    SGD = 'SGD'

def get_optimizer(optimizer: Optimizers | str, model: torch.nn.Module, **kwargs) -> torch.optim.Optimizer:
    if isinstance(optimizer, str):
        optimizer = Optimizers(optimizer)

    if optimizer == Optimizers.Adam:
        return torch.optim.Adam(model.parameters(), **kwargs)
    elif optimizer == Optimizers.AdamW:
        return torch.optim.AdamW(model.parameters(), **kwargs)
    elif optimizer == Optimizers.SGD:
        return torch.optim.SGD(model.parameters(), **kwargs)
    elif optimizer == Optimizers.RMSprop:
        return torch.optim.RMSprop(model.parameters(), **kwargs)
    elif optimizer == Optimizers.Adagrad:
        return torch.optim.Adagrad(model.parameters(), **kwargs)
    elif optimizer == Optimizers.Adadelta:
        return torch.optim.Adadelta(model.parameters(), **kwargs)
    elif optimizer == Optimizers.ASGD:
        return torch.optim.ASGD(model.parameters(), **kwargs)
    elif optimizer == Optimizers.NAdam:
        return torch.optim.NAdam(model.parameters(), **kwargs)
    elif optimizer == Optimizers.LBFGS:
        return torch.optim.LBFGS(model.parameters(), **kwargs)
    elif optimizer == Optimizers.SparseAdam:
        return torch.optim.SparseAdam(model.parameters(), **kwargs)
    elif optimizer == Optimizers.Adamax:
        return torch.optim.Adamax(model.parameters(), **kwargs)
    else:
        raise ValueError(f"Unsupported optimizer: {optimizer}")


class ttt:  # todo make a better class name?
    def __init__(self,
                 model: torch.nn.Module,
                 train: torch.utils.data.DataLoader,
                 test: torch.utils.data.DataLoader = None,
                 validation: torch.utils.data.DataLoader = None,
                 # todo figure out a good way to select parameters as well
                 optimizer: Optimizers = None,
                 loss_fn: callable = None,
                 device: torch.device | str = None,
                 epochs: int = 10,
                 use_amp: bool = False,
                 show_metrics: bool = True,
                 plot_loss: bool = True,
                 dir: str | Path | os.PathLike = None,
                 verbose: bool = False,
                 *args, **kwargs):

        self.verbose = verbose

        self._train_loader = train
        self._validation_loader = validation
        self._test_loader = test

        self.model = model
        self.device = device or get_optimal_device(verbose=self.verbose)
        self.optimizer = get_optimizer(optimizer, self.model, **kwargs) if optimizer else torch.optim.Adam(self.model.parameters())
        self.loss_fn = loss_fn or torch.nn.CrossEntropyLoss() #! beware for multiclass implementation
        self.dir = dir

        self.epochs = epochs


    @property
    def train_loader(self):
        return self._train_loader

    @train_loader.setter
    def train_loader(self, loader: torch.utils.data.DataLoader):
        if not isinstance(loader, torch.utils.data.DataLoader):
            raise ValueError(
                "train_loader must be an instance of torch.utils.data.DataLoader")
        self._train_loader = loader

    @property
    def validation_loader(self):
        return self._validation_loader

    @validation_loader.setter
    def validation_loader(self, loader: torch.utils.data.DataLoader):
        if not isinstance(loader, torch.utils.data.DataLoader):
            raise ValueError(
                "validation_loader must be an instance of torch.utils.data.DataLoader")
        self._validation_loader = loader

    @property
    def test_loader(self):
        return self._test_loader

    @test_loader.setter
    def test_loader(self, loader: torch.utils.data.DataLoader):
        if not isinstance(loader, torch.utils.data.DataLoader):
            raise ValueError(
                "test_loader must be an instance of torch.utils.data.DataLoader")
        self._test_loader = loader

    def train(self):
        self.model.train()
        self.model.to(self.device)

        best_val_loss = float('inf')

        for epoch in range(1, self.epochs + 1):
            self.model.train()
            total_loss = 0.0

            for (data, target) in tqdm(self.train_loader):
                data, target = data.to(self.device), target.to(self.device)

                self.optimizer.zero_grad()
                output = self.model(data)
                loss = self.loss_fn(output, target)
                loss.backward()
                self.optimizer.step()

                total_loss += loss.item()

            avg_loss = total_loss / len(self.train_loader)
            print(f'Epoch {epoch}, Training Loss: {avg_loss:.4f}')

            if self.validation_loader is not None: # todo move this to self.validate
                val_loss = self.validate()
                if val_loss < best_val_loss:
                    best_val_loss = val_loss
                    # print(f'New best validation loss: {best_val_loss:.4f}')
                    # Save the best model
                    if self.dir is not None: #!
                        torch.save(self.model.state_dict(), Path(self.dir) / f'best_model.pth')

    def learn(self):
        """Alias for train in case user wants to say 'machine.learn()'"""
        self.train()

    def validate(self):
        if self.validation_loader is None:
            raise ValueError("Cannot validate with no validation set")

    def test(self):
        if self.test_loader is None:
            raise ValueError("Cannot test with no test set")

    def hyperparameter_search(self) -> dict:
        pass  # todo - this will probably be a bit complex

    def __str__(self) -> str:
        optimizer_params = self.optimizer.param_groups[0]
        optimizer_params.pop('params', None)  # remove params for cleaner output

        return f"""
Torch Train Tester (TTT):
    model            = {self.model.__class__.__name__}
    device           = {self.device}
    epochs           = {self.epochs}
    optimizer        = {self.optimizer.__class__.__name__}
    optimizer_params = {'\n' + ',\n'.join(f'\t{k}={v}' for k, v in optimizer_params.items())}
    train_size       = {len(self.train_loader.dataset)}
    validation_size  = {len(self.validation_loader.dataset) if self.validation_loader is not None else 0}
    test_size        = {len(self.test_loader.dataset) if self.test_loader is not None else 0}
"""
# optimizer_defaults={self.optimizer.defaults}

    def __hash__(self):
        pass # todo

    def __repr__(self):
        pass # todo

if __name__ == "__main__":
    # ttt()
    pass
