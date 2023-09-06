import torch
from torch.utils.data import Dataset, Dataloader
from torchvision import transforms
import pandas as pd
from PIL import Image

class EmbryoDataset(Dataset):
    def __init__ (self, csv_path, transform=None):
        self.data = pd.read_csv(csv_path)
        self.transform = transform

    def __len__(self):
        return len(self.data)
    
    def __getitem__ (self, index):
        img_path = self.data.iloc[index, 0]
        image = Image.open(img_path)
        label = self.data.iloc[index, 1]
        if self.transform:
            image = self.transform(image)
        
        return image, label
    
