import numpy as np
import matplotlib.pyplot as plt

def main():

    plt.axes(aspect="equal")
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    for r in [1, 2, 3, 4]:
        t = np.linspace(0, 2 * np.pi)
        x = r * np.cos(t)
        y = r * np.sin(t)
        plt.plot(x, y, color="black")
    plt.savefig("rotation.png")

if __name__ == "__main__":
    main()
