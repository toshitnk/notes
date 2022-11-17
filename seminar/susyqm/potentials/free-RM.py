import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
V1 = 1-2/np.cosh(x)
V2 = x/x
plt.plot(x, V1, label="Rosen-Morse")
plt.plot(x, V2, color="black", linestyle="dashed", label="freee particle")
plt.legend()
plt.savefig("./free-RM.png")
