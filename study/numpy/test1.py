#https://numpy.org/doc/stable/user/quickstart.html#an-example
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)
print(a.size)
print(type(a))