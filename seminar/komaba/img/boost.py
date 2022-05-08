import numpy as np
import matplotlib.pyplot as plt

def main():

    plt.axes(aspect="equal")
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    for r in [1, 2, 3, 4]:
        t = np.linspace(-3, 3)
        x = r * np.cosh(t)
        y = r * np.sinh(t)
        plt.plot(x, y, color="black")
        plt.plot(-x, y, color="black")
        plt.plot(y, x,color="black")
        plt.plot(y, -x, color="black")
    plt.savefig("boost.png")

if __name__ == "__main__":
    main()
