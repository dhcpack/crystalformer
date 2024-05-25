import torch

a = torch.tensor([1, 2, 3], dtype=torch.float32)
print(a.size())
a = a[None]
print(a.size())