# backtracking.py

# Andrew Cunningham
# CSC506 Portfolio Project

# implements backtracking

def backtrack(dtw_matrix):
    # get the length of each array
    i, j = dtw_matrix.shape[0] - 1, dtw_matrix.shape[1] - 1
    path = []

    # backtrack, starting at the bottom left, across the matrix diagonal
    while i > 0 and j > 0:
        # save the next diagonal step
        path.append((i-1, j-1))

        # evaluate either diagronal, up, or left
        diag = dtw_matrix[i-1, j-1]
        up = dtw_matrix[i-1, j]
        left = dtw_matrix[i, j-1]

        # move to the neighbor with the lowest cost
        if diag <= up and diag <= left:
            i = i-1
            j = j-1
        elif up < left:
            i = i-1
        else:
            j = j-1
    
    path.reverse()
    return path