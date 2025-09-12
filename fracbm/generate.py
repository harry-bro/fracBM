import numpy as np
from .covariance import fBMcov, toeplitz

#fbm via Cholensky decomp
def cholesky(n, H):
    z = np.random.normal(0, 1, n)
    try:
        L = np.linalg.cholesky(fBMcov(n, H))
    except np.linalg.LinAlgError:
        # need +ve eigenvalues for SPD. So adding small epsilon to trace will prevent slightly -ve eigenvalues due to floating point precision
        cov += 1e-15 * np.eye(n)
        L = np.linalg.cholesky(cov)
    B = np.linalg.matmul(L, z)
    return B

#fbm via Davies-Harte
def daviesharte(n, H):

    #constructing circulant toeplitz covariance vector
    indices = np.arange(n) 
    g = toeplitz(np.arange(n), H)
    c = np.concatenate([g, [0], g[1:][::-1]])
    lam = np.fft.fft(c) 
    lam = np.real_if_close(np.fft.fft(c))
    lam = np.maximum(lam, 0.0)
    
    #create gaussian variables in fourier space
    Z = np.zeros(2*n, dtype=complex)
    Z[0] = np.random.normal()
    Z[n] = np.random.normal()
    U = np.random.normal(size=n-1)
    V = np.random.normal(size=n-1)
    Z[1:n] = (U + 1j*V) / np.sqrt(2)
    Z[n+1:] = np.conj(Z[1:n][::-1])

    Ytilda = Z * np.sqrt(lam)
    Y = np.fft.ifft(Ytilda).real * np.sqrt(2*n)

    X = Y[:n]
    B = np.cumsum(X)
    return B
    
