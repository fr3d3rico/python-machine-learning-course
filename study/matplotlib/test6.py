import numpy as np
from scipy import stats

#array = np.arange(10)
#array = [0,1,2,0,3]
array = np.array([0,1,2,0,2,1])
print(array)
print(np.sort(array))

r1 = np.mean(array)
print(f'Mean {r1}')

r3 = np.var(array)
print(f'Variance {r3}')

r2 = np.std(array)
print(f'Standard deviation {r2}')

r4 = np.median(array)
print(f'Median {r4}')

r5 = stats.mode(array, axis=None)
print(f'Mode {r5}')

r5 = stats.mode(array)
print(f'Mode {r5}')