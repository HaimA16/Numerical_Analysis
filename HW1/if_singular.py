from Numerical_Analysis.HW1.best_diagonal import get_best_diagonal


def check_if_singular(mat, b, n):
    singular_flag = get_best_diagonal(mat, n)
    if singular_flag != -1:
        if b[singular_flag]:
            print("Singular Matrix (Inconsistent System)")
            return 0
        else:
            print("Singular Matrix (May have infinitely many solutions)")
            return 0
    return -1