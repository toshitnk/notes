import numpy as np
import matplotlib.pyplot as plt

p1 = np.linspace(1/4, 1, 50)
p2 = np.linspace(1, 2, 50)

y1 = (((4*p1-1)/3)**(3/2))/2
y2 = (p2**2 + 2*p2 - 2)/2

plt.plot(p1, y1)
plt.scatter([1], [1/2], color="blue")
plt.plot(p2, y2, color="black")

plt.savefig("../img/eg2_legendre.png")
