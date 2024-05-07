import matplotlib.pyplot as plt
import numpy as np

from typing import Callable


def style_axis(
    ax: plt.axes,
    xlab: str = "",
    ylab: str = "",
    xgrid: bool = True,
    ygrid: bool = True,
    lab_size: int = 11,
) -> None:
    ax.minorticks_on()
    ax.spines[["top", "right"]].set_visible(False)

    if xlab:
        ax.set_xlabel(xlab, fontsize=lab_size)
    if ylab:
        ax.set_ylabel(ylab, fontsize=lab_size)

    if xgrid:
        ax.xaxis.grid(True, which="major", color="gray", alpha=0.6, linewidth=0.5)
        ax.xaxis.grid(
            True, which="minor", color="gray", alpha=0.6, linewidth=0.2, linestyle="--"
        )
    if ygrid:
        ax.yaxis.grid(True, which="major", color="gray", alpha=0.6, linewidth=0.5)
        ax.yaxis.grid(
            True, which="minor", color="gray", alpha=0.6, linewidth=0.2, linestyle="--"
        )


def rk4(
    fprime: Callable,
    timespan: tuple[float, float],
    y0: list[float],
    h: float = 0.1,
) -> tuple:
    """Fourth-Order Runge-Kutta method for solving ODEs"""

    x0, xend = timespan
    X = np.array([x0 + i * h for i in range(int(np.ceil((xend - x0) / h)))])
    Y = np.empty((len(X), len(y0)))
    Y[0, :] = y0

    for i in range(1, X.shape[0]):
        K1 = h * fprime(X[i - 1], Y[i - 1, :])
        K2 = h * fprime(X[i - 1] + h / 2, Y[i - 1, :] + K1 / 2)
        K3 = h * fprime(X[i - 1] + h / 2, Y[i - 1, :] + K2 / 2)
        K4 = h * fprime(X[i - 1] + h, Y[i - 1, :] + K3)
        Y[i, :] = Y[i - 1, :] + (K1 + 2 * K2 + 2 * K3 + K4) / 6

    return X, Y
