from Numerical_Analysis.HW1.swap_row import swap_row


def get_best_diagonal(mat, n):
    for i in range(n):
        pivot_row = i
        v_max = mat[pivot_row][i]
        for j in range(i + 1, n):
            if abs(mat[j][i]) > abs(v_max):
                v_max = mat[j][i]
                pivot_row = j

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.
        if not mat[pivot_row][i]:
            return i  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != i:
            swap_row(mat, i, pivot_row)
    return -1
