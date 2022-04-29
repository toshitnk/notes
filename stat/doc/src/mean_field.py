import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.tanh(0.7*x)
z = np.tanh(1.3*x)

plt.ylim(-1.5, 1.5)
plt.plot(x, x, label=r"$y = x$")
plt.plot(x, y, label=r"$T > T_c$")
plt.plot(x, z, label=r"$T < T_c$")
plt.scatter([-0.752, 0, 0.752], [-np.tanh(1.3 * 0.752), 0, np.tanh(1.3 * 0.752)])
plt.legend()
plt.savefig("./img/mean_field.png")
