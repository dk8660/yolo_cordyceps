import torch
import utils
display = utils.notebook_init()  # checks
USE_CUDA = torch.cuda,torch.is_vulkan_available()
print(USE_CUDA)
device = torch.device('cuda:0' if USE_CUDA else 'cpu')
print(device)
print(torch.cuda.get_device_name(0))