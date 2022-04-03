import numpy as np
import matplotlib.pyplot as plt

def f(array):
    i = 0
    ans = np.zeros(len(array))
    while array[i] < 1:
        x = array[i]
        ans[i] = (((4*x-1)/3)**(3/2))/2
        i = i+1
    while i < len(array):
        x = array[i]
        ans[i] = (x**2 + 2*x - 2)/2
        i = i+1
    return ans

x = np.linspace(1/4 , 3, 100)
ans = f(x)
plt.plot(x, ans, label="f*(x)")
plt.savefig("../img/eg2_legendre.png")
