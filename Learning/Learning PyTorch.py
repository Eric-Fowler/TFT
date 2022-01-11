import torch
tensor1 = torch.tensor([1])
tensor2 = torch.tensor([2])
sum = tensor1+tensor2
sum = sum.numpy()
print(sum[0])