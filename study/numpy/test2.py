#https://numpy.org/doc/stable/user/quickstart.html#an-example
import numpy as np
a = np.array([2,3,4])
print(a)

b = np.arange(12)
print(b)

b = b.reshape(2,6)
print(b)

print(np.arange(10000).reshape(100,100))