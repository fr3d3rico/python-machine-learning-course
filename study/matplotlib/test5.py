import numpy as np
import matplotlib.pyplot as p

print(np.random.randn(10))

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

print(x)

n, bins, patches = p.hist(x, 50, density=1, facecolor='g', alpha=0.75)

p.xlabel('Smarts')
p.ylabel('Probability')
p.title('Histogram of IQ')
p.text(60, .025, r'$\mu=100,\ \sigma=15$')
p.axis([40, 160, 0, 0.03])
p.grid(True)
p.show()