import numpy as np

a = [1, 2, 3, 4]
b = [1, 2, 4, 3]

#mean
print(f'mean(a) = {np.mean(a)} variation(a) = {np.var(a)} standard deviation(a) = {np.std(a)}')
print(f'mean(b) = {np.mean(b)} variation(b) = {np.var(b)} standard deviation(b) = {np.std(b)}')

print(np.cov(a, b))
print(np.corrcoef(a, b))