import numpy as np

from Numerical_Analysis.HW1.jacobi import get_jacobi_solution
from Numerical_Analysis.HW1.gauss_seidel import gauss_seidel
if __name__ == '__main__':
    mat = np.array([[4, 2, 0],
                    [2, 10, 4],
                    [0, 4, 5]])
    n = len(mat)
    b = np.array([2, 6, 5])
    x = np.zeros_like(b, dtype=np.double)

    soloution = input("Enter the method you want to use\n 1.jacobi.\n 2.gauss_seidel.\n")
    if soloution == '1':
        get_jacobi_solution(mat, b, n, x)
    elif soloution == '2':
        gauss_seidel(mat, b, x)
    else:
        print("Invalid input")