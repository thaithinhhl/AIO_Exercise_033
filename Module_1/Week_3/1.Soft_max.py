import torch
import torch.nn as nn
import torch.nn.functional as F


class soft_max(nn.Module):
    def __init__(self):
        super(soft_max, self).__init__()

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)


class soft_max_stable(nn.Module):
    def __init__(self):
        super(soft_max_stable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        return torch.exp(x-c) / torch.sum(torch.exp(x - c), dim=0)


x = torch.tensor([1, 2, 3])

softmax = soft_max()
softmaxstable = soft_max_stable()

print(softmax(x))
print(softmaxstable(x))
