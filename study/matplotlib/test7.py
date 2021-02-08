from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

#Normal / Gaussian
x = np.arange(-3, 3, 0.0001)
print(x)

plt.plot(x, norm.pdf(x))
plt.show()

#exponential
from scipy.stats import expon
x = np.arange(0, 10, 0.001)
plt.plot(expon.pdf(x)) #Probability density function
plt.show()

#binomial
from scipy.stats import binom
n, p = 10, 0.5
x = np.arange(0, 10, 0.1)
plt.plot(x, binom.pmf(x, n, p)) #Probability mass function
plt.show()
print(len(x))

#poisson
from scipy.stats import poisson
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()
print(len(x))