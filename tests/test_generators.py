import numpy as np
import fracbm.cholesky as ch
import fracbm.daviesharte as dh

def test_cholesky_noise_shape():
    n = 100
    H = 0.7
    x = ch.noise(n, H)
    assert isinstance(x, np.ndarray)
    assert x.shape == (n,)

def test_cholesky_motion_length():
    n = 200
    H = 0.6
    # motion returns cumulative sum of noise
    B, x = ch.motion(n, H, return_noise=True)
    assert isinstance(B, np.ndarray)
    assert B.shape == (n,)
    np.testing.assert_allclose(B, np.cumsum(x), rtol=1e-12)

def test_daviesharte_noise_shape():
    n = 100
    H = 0.8
    x = dh.noise(n, H)
    assert isinstance(x, np.ndarray)
    assert x.shape == (n,)

def test_daviesharte_motion_cumsum():
    n = 50
    H = 0.5
    B, x = dh.motion(n, H, return_noise=True)
    assert isinstance(B, np.ndarray)
    assert B.shape == (n,)
    np.testing.assert_allclose(B, np.cumsum(x), rtol=1e-12)
