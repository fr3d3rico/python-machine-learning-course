import matplotlib.pyplot as p

p.plot([1,2,3,4], [1,4,9,16])
p.show()

p.plot([1,2,3,4], [1,4,9,16], 'ro')
p.axis([0,6, 0,20])
p.show()

import numpy as np

t = np.arange(0. , 5. , 0.2)
p.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
p.show()


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

p.scatter('a', 'b', c='c', s='d', data=data)
p.xlabel('entry a')
p.ylabel('entry b')
p.show()



names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

p.figure(figsize=(9, 3))

p.subplot(131)
p.bar(names, values)
p.subplot(132)
p.scatter(names, values)
p.subplot(133)
p.plot(names, values)
p.suptitle('Categorical Plotting')
p.show()


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

print(t1)

p.figure()
p.subplot(211)
p.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

p.subplot(212)
p.plot(t2, np.cos(2*np.pi*t2), 'r--')
p.show()