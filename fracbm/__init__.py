"""
fracbm: Fractional Brownian Motion generators
=============================================

Provides exact methods for generating
fractional Gaussian noise (fGn) and fractional Brownian motion (fBm).

Hurst exponent estimation using Wavelet method.

Available methods:
- fracbm.cholesky.noise(n, H)
- fracbm.cholesky.motion(n, H)
- fracbm.daviesharte.noise(n, H)
- fracbm.daviesharte.motion(n, H)
- fracbm.invhurst.estimate(X)
"""

from . import cholesky
from . import daviesharte
from . import invhurst

__all__ = ["cholesky", "daviesharte", "invhurst"]

__version__ = "0.3.0"
