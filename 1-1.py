import torch
x = torch.arange(4.0, requires_grad = True)
y=2*torch.dot(x, x)

y.backward()
x.grad.zero_()
y = x.sum()
y.backward()
print(x.grad)