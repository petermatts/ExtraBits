from enum import StrEnum
from pathlib import Path
import os
import torch

# a torch train tester for all use cases


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

# def DefaultOptimizerParams(optimizer: Optimizers) -> dict:


class ttt:  # todo make a better class name?
    def __init__(self,
                 model: torch.nn.Module,
                 train: torch.utils.data.DataLoader,
                 test: torch.utils.data.DataLoader = None,
                 validation: torch.utils.data.DataLoader = None,
                 # todo figure out a good way to select parameters as well
                 optimizer: Optimizers = None,
                 optimizer_hyperparameters: dict = {},
                 loss_fn: callable = None,
                 device: torch.device | str = None,
                 epochs: int = 10,
                 use_amp: bool = False,
                 show_metrics: bool = True,
                 plot_loss: bool = True,
                 dir: str | Path | os.PathLike = None,
                 *args, **kwargs):

        self._train_loader = train
        self._validation_loader = validation
        self._test_loader = test

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
        pass  # todo

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


if __name__ == "__main__":
    # ttt()
    pass
