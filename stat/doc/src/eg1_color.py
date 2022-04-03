import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 1, 50)
x2 = np.linspace(1, 2, 50)
x3 = np.linspace(2, 3, 50)

y1 = (x1**3 + x1)/4
y2 = x2 - 1/2
y3 = x3**2/2 - x3 + 3/2

plt.plot(x1, y1)
plt.plot(x2, y2, color="blue")
plt.plot(x3, y3, color="black")

plt.savefig("../img/eg1_legendre.png")
