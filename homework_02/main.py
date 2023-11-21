import matplotlib.pyplot as plt
import numpy as np

def f(x1, x2):
    return 8 * x1 + 12 * x2 + x1 ** 2 - 2 * x2 ** 2


vecf = np.vectorize(f)

x1, x2 = np.meshgrid(np.linspace(-10,2,100), np.linspace(-4,10,100))

fig, ax = plt.subplots(1)
ax.contour(x1,x2, vecf(x1,x2), 30)
ax.plot(-4,3,'ro')

## Generate plot for Homework 2 | 1b)
plt.savefig("test.svg", format="svg")
plt.show()