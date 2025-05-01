# dtw.py

# Andrew Cunningham
# CSC506 Portfolio Project

# implements Dynamic Time Warping between two input vectors.

import numpy as np

def dtw(upper, lower, window=None):
    '''implements DTW between upper: List[int] and lower: List[int]
        Returns dtw_matrix(n x m)'''
    n, m = len(upper), len(lower)
    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0

    for i in range(1, n+1):
        j_start = max(1, i - window) if window is not None else 1
        j_end = min(m+1, i + window + 1) if window is not None else m + 1
        for j in range(j_start, j_end):
            cost = abs(upper[i-1] - lower[j-1])
            last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min

    return dtw_matrix