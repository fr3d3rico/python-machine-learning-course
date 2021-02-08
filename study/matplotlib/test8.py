#percentiles
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp 

print(np.version.version)

vals = np.random.normal(0, 0.5, 10000)
plt.hist(vals, 50)
plt.show()

print(np.percentile(vals, 50))
print(np.percentile(vals, 10))
print(np.percentile(vals, 90))

#moments: mean
print(np.mean(vals))

#moments: variance
print(np.var(vals))

#moments: skew
print(sp.skew(vals))

#moments: kurtosis
print(sp.kurtosis(vals))