import numpy as np

#generating the two types of covariance needed

#standard fbm covariance
def fBMcov(n, H):
    times = np.arange(1, n+1)
    i_mat, j_mat = np.meshgrid(times, times, indexing ='ij')

    cov = (1/2) * (i_mat**(2*H) + j_mat**(2*H) - np.abs(i_mat - j_mat)**(2*H))
    return cov

#toeplitz autocovariance
def toeplitz(k, H):
    k = np.asarray(k)
    return 0.5 * ((np.abs(k+1)**(2*H)) - 2*(np.abs(k)**(2*H)) + (np.abs(k-1)**(2*H)))