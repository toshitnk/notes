import numpy as np
import matplotlib.pyplot as plt

def f(array):
    i = 0
    ans = np.zeros(len(array))
    while array[i] < 1:
        x = array[i]
        ans[i] = (x**3 + x) / 4
        i = i+1
    while array[i] < 2:
        x = array[i]
        ans[i] = x - 1/2
        i = i+1
    while i < len(array):
        x = array[i]
        ans[i] = x**2 / 2 - x + 3/2
        i = i+1
    return ans

x = np.linspace(0, 5, 100)
ans = f(x)
plt.plot(x, ans, label="f(x)")
plt.savefig("../img/eg1_legendre.png")
