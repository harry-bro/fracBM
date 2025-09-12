import numpy as np
from scipy.linalg import toeplitz


#generating the two types of covariance needed

#standard fbm covariance
def fBMcov(n, H):
    times = np.arange(1, n+1)
    i_mat, j_mat = np.meshgrid(times, times, indexing ='ij')

    cov = (1/2) * (i_mat**(2*H) + j_mat**(2*H) - np.abs(i_mat - j_mat)**(2*H))
    return cov

def toeplitzVEC(n, H):
    """Return 1D autocovariance vector for fBm of length n"""
    k = np.arange(n)
    return 0.5 * ((np.abs(k+1)**(2*H)) - 2*(np.abs(k)**(2*H)) + (np.abs(k-1)**(2*H)))


def toeplitzMAT(n, H):
    """Return Toeplitz covariance matrix of size (n, n)"""
    r = toeplitzVEC(n, H)  # 1D vector
    return toeplitz(r)      # full (n,n) matrix
