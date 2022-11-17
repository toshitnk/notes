import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/2, np.pi/2, 100)

V1 = -x/x
V2 = 2/(np.cos(x))**2 - 1

plt.plot(x, V1, label="rectangle")
plt.ylim(-1.5, 10)
plt.plot(x, V2, color="black", label="Poeschl-Teller", linestyle="dashed")
plt.legend()
plt.savefig("./rectangle-PT.png")
