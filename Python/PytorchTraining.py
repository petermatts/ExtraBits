"""
@file: PytorchTraining.py

After working for pytorch for a while, one of the most tedious steps of setting up a project is
setting up functions like a train function. In this file my goal is to write well designed
function(s) to support this task that can be copied and pasted into any other project and work
seemlessly.
"""

import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

def test(loader: DataLoader, model: torch.nn.Module, criterion, disable_print: bool = False,
         msg: str = "", device = torch.device("cuda" if torch.cuda.is_available() else "cpu")) -> float:
    """
    Check the accuracy of a classification model.
    
    Inputs:
    - loader: A DataLoader for the data split we want to check
    - model: torch model to test the accudacy of
    - disable_print: disables accuracy print statement if True, default False
    - msg: optional preamble to the accuracy print (leading white space is stripped)
    - device: the device evaluate model on
    
    Returns: Model accuracy on the provided data
    """
    num_correct = 0
    num_samples = 0
    model.eval()  # set model to evaluation mode
    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)  # move to device, e.g. GPU
            y = y.to(device=device, dtype=torch.long)
            scores = model(x)
            loss = criterion(scores, y)
            _, preds = scores.max(1)
            num_correct += (preds == y).sum()
            num_samples += preds.size(0)
        acc = float(num_correct) / num_samples

        if not disable_print:
            print(f"{msg} accuracy {'%3.3f'%(100*acc)} ({num_correct}/{num_samples})".lstrip())

    return acc, loss


def study(model: torch.nn.Module, optimizer: torch.optim.Optimizer,
          loader_train: DataLoader, loader_val: DataLoader,
          criterion = torch.nn.CrossEntropyLoss(),
          epochs: int = 1, disable_print: bool = False,
          device = torch.device("cuda" if torch.cuda.is_available() else "cpu")) -> tuple[list, list]:
    """
    Train a model on CIFAR-10 using the PyTorch Module API.
    
    Inputs:
    - model: A PyTorch Module giving the model to train.
    - optimizer: An Optimizer object we will use to train the model
    - loader_train: torch DataLoader for the training data
    - loader_val: torch DataLoader for the validation data
    - criterion: loss function, default is cross entropy loss
    - epochs: (Optional) A Python integer giving the number of epochs to train for
    - disable_print: disables periodic accuracy prints if True, defualt False
    - device: the device to run training on
    
    Returns: List of losses at every iteration and a list of validation accuracies at every epoch
    """

    loss_log = list()
    log_val = list()

    model = model.to(device=device)  # move the model parameters to CPU/GPU
    for e in range(epochs):
        for t, (x, y) in enumerate(tqdm(loader_train, desc=f"Epoch ({e+1:{len(str(epochs))}}/{epochs})")):
            model.train()  # put model to training mode
            x = x.to(device=device)  # move to device, e.g. GPU
            y = y.to(device=device, dtype=torch.long)

            scores = model(x)
            loss = criterion(scores, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            loss_log.append(loss.item())

        if not disable_print:
            print('Loss = %.4f' % (loss.item()))
        acc, _ = test(loader_val, model, criterion, msg = "Validation",
                             disable_print=disable_print, device=device)
        log_val.append(acc)
    
    return loss_log, log_val #? return validation accuracies too?
