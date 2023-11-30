from timeit import timeit

import numpy as np

L = range(1000)

print(timeit(i**2 for i in L))

a = np.arange(1000)
print(timeit(a ** 2))
