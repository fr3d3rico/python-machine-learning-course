import matplotlib.pyplot as plt
import numpy as np

a = np.arange(4)
b = np.arange(4)
#c = np.linear()

fig, ax = plt.subplots()
#ax.plot(a, b)
ax.plot(a, b, label='linear')
ax.plot(a, b**2, label='quadratic')
ax.plot(a, b**3, label='cubic') 

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('MatplotLib study!')
ax.legend()

plt.show()
fig.savefig('test1') # fig and not ax or plt Fred!
