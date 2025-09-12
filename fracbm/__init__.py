"""
fracbm: Fractional Brownian Motion generators
=============================================

Provides exact methods for generating
fractional Gaussian noise (fGn) and fractional Brownian motion (fBm).

Available methods:
- fracbm.cholesky.noise(n, H)
- fracbm.cholesky.motion(n, H)
- fracbm.daviesharte.noise(n, H)
- fracbm.daviesharte.motion(n, H)
"""

from . import cholesky
from . import daviesharte

__all__ = ["cholesky", "daviesharte"]

__version__ = "0.2.1"
