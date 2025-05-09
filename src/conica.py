# flake8: noqa
import numpy as np
import matplotlib.pyplot as plt


def plot_conic(A, B, C, D, E, F, xlim=(-10, 10), ylim=(-10, 10), resolution=400):

    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    X, Y = np.meshgrid(x, y)

    Z = (A * X**2 + B * X * Y + C * Y**2 +
         D * X + E * Y + F)

    plt.figure(figsize=(6, 6))
    plt.contour(X, Y, Z, levels=[0], linewidths=2)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.title(f'Conica: {A}x² + {B}xy + {C}y² + {D}x + {E}y + {F} = 0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().set_aspect('equal', 'box')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    A = float(input("A = "))
    B = float(input("B = "))
    C = float(input("C = "))
    D = float(input("D = "))
    E = float(input("E = "))
    F = float(input("F = "))

    plot_conic(A, B, C, D, E, F)
