import numpy as np
import pywt
from .utils import weighted_least_squares

def estimate(X):
    '''Returns the hurst index of a given signal (mininum length of ~500)'''
    wavelet = 'db3' #3 vanishing moments
    coeffs = pywt.wavedec(X, wavelet=wavelet, level=None)[1:]
    nj = np.array([len(c) for c in coeffs])

    variances = [np.mean(d**2) for d in coeffs] #empirical variances
    J = len(coeffs)

    j_indices = np.arange(J, 0, -1)
    mask = (j_indices >=3) & (j_indices <= J-2)
    x = j_indices[mask]
    wj = nj[mask]

    S = np.log2(np.array(variances)[mask])
    _, m = weighted_least_squares(x, S, wj)

    return (m-1)/2