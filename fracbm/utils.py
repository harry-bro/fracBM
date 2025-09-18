import numpy as np
from scipy.linalg import toeplitz # type: ignore


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


def weighted_least_squares_matrix(x, y, weights):
    X = np.vstack([np.ones(len(x)), x]).T
    Y = np.asarray(y)
    W = np.diag(weights)
    beta = np.linalg.inv(X.T @ W @ X) @ (X.T @ W @ Y)
    return beta

def weighted_least_squares(x, y, w):
    W = np.sum(w)
    x_bar = np.sum(w * x) / W
    y_bar = np.sum(w * y) / W

    num = np.sum(w * (x - x_bar) * (y - y_bar))
    den = np.sum(w * (x - x_bar)**2)
    m = num / den

    a = y_bar - m * x_bar

    return a, m