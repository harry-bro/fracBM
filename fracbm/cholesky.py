import numpy as np
from .utils import toeplitzMAT

def noise(n: int, H: float) -> np.ndarray:
    """
    Generate fractional Gaussian noise (fGn) using Cholesky decomposition.

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
    z = np.random.normal(0, 1, n)
    cov = toeplitzMAT(n, H)  # full (n, n) covariance matrix

    try:
        L = np.linalg.cholesky(cov)
    except np.linalg.LinAlgError:
        # Fix nearly non-SPD covariance by nudging the diagonal
        cov += 1e-15 * np.eye(n)
        L = np.linalg.cholesky(cov)

    return L @ z


def motion(n: int, H: float, return_noise: bool = False) -> np.ndarray:
    """
    Generate fractional Brownian motion (fBm) using Cholesky decomposition.

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
