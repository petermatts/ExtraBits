from ttt import ttt
from torch.utils.data import Dataset, DataLoader
from pathlib import Path
from torchvision import datasets, transforms


class MNIST(Dataset):
    def __init__(self, train: bool = True, transform: transforms.Compose = None, download: bool = False):
        self.root = Path(__file__).parent / "data"
        self.train = train

        default_transform = transforms.Compose([
            transforms.ToTensor()  # Convert PIL Image to Tensor
        ])
        self.transform = transform or default_transform

        # Loading the data using datasets.MNIST to avoid re-downloading
        # We'll access the data files and labels manually
        self.data = datasets.MNIST(
            root=self.root, train=self.train, download=download, transform=self.transform)

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> tuple:
        image, label = self.data[index]
        return image, label


if __name__ == "__main__":
    # Initialize the MNIST train dataset
    train = MNIST()

    # Create a DataLoader to load the data in batches
    train_loader = DataLoader(train, batch_size=64, shuffle=True)

    # Iterate through the DataLoader and print out the first batch
    for images, labels in train_loader:
        # Should print torch.Size([64, 1, 28, 28]) torch.Size([64])
        print(images.shape, labels.shape)
        break  # Just print the first batch to verify
