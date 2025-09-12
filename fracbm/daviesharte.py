import numpy as np
from .utils import toeplitzVEC

def noise(n: int, H: float) -> np.ndarray:
    """
    Generate fractional Gaussian noise (fGn) using the Davies–Harte method.

    Parameters
    ----------
    n : int
        Number of increments
    H : float
        Hurst parameter (0 < H < 1)

    Returns
    -------
    np.ndarray
        Array of Gaussian increments
    """
    # Autocovariance vector (1D)
    r = toeplitzVEC(n, H)
    c = np.concatenate([r, [0], r[1:][::-1]])  # all 1D arrays
    lam = np.fft.fft(c).real
    lam = np.maximum(lam, 0)  # remove negative eigenvalues

    # Generate complex Gaussian variables
    Z = np.zeros(2 * n, dtype=complex)
    Z[0] = np.random.normal()
    Z[n] = np.random.normal()
    U = np.random.normal(size=n-1)
    V = np.random.normal(size=n-1)
    Z[1:n] = (U + 1j * V) / np.sqrt(2)
    Z[n+1:] = np.conj(Z[1:n][::-1])

    Ytilda = Z * np.sqrt(lam)
    Y = np.fft.ifft(Ytilda).real * np.sqrt(2 * n)

    # fGn is first n increments
    return Y[:n]


def motion(n: int, H: float, return_noise: bool = False) -> np.ndarray:
    """
    Generate fractional Brownian motion (fBm) using the Davies–Harte method.

    Parameters
    ----------
    n : int
        Number of steps
    H : float
        Hurst parameter

    Returns
    -------
    np.ndarray
        Fractional Brownian motion path
    """
    x = noise(n, H)
    B = np.cumsum(x)
    if return_noise:
        return B, x
    return B
