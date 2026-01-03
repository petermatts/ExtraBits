from ttt import ttt
from torch import nn
from torch.utils.data import Dataset, DataLoader
from pathlib import Path
from torchvision import datasets, transforms
import argparse


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

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.pool(x)
        x = self.relu(self.conv2(x))
        x = self.pool(x)
        x = x.view(-1, 64 * 7 * 7)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--downlaod", action="store_true",
                        help="Whether to download the MNIST dataset")
    args = parser.parse_args()

    # Initialize the MNIST train dataset
    train = MNIST(download=args.downlaod)

    # Create a DataLoader to load the data in batches
    train_loader = DataLoader(train, batch_size=64, shuffle=True)

    # Iterate through the DataLoader and print out the first batch
    for images, labels in train_loader:
        # Should print torch.Size([64, 1, 28, 28]) torch.Size([64])
        print(images.shape, labels.shape)
        break  # Just print the first batch to verify

    # Initialize the CNN model
    cnn = CNN()

    # train the model with ttt
    model = ttt(cnn, train_loader, epochs=1)
    model.train()

    print(model)
