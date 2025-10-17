"""
I just want to see if I can use CUDA acceleration for pytorch now that I have CUDA on my computer
"""

import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(torch.cuda.current_device))
