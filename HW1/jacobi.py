import numpy as np
from numpy.linalg import norm

from Numerical_Analysis.HW1.best_diagonal import get_best_diagonal
from Numerical_Analysis.HW1.if_singular import check_if_singular
from Numerical_Analysis.HW1.is_diagonaly_dominant import is_diagonally_dominant



def get_D(mat, n):
    D = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = mat[i][j]
    return D


def get_L(mat, n):
    L = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        for j in range(n):
            if i > j:
                L[i][j] = mat[i][j]
    return L


def get_U(mat, n):
    U = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        for j in range(n):
            if i < j:
                U[i][j] = mat[i][j]
    return U


def get_jacobi_H(mat, n):
    return np.linalg.inv(get_D(mat, n))


def get_jacobi_G(mat, n):
    inverse_of_D = np.linalg.inv(get_D(mat, n))
    L_plus_U = get_L(mat, n) + get_U(mat, n)
    return np.dot(inverse_of_D, L_plus_U)*(-1)


def jacobi_iterative(mat, b, n, X0, TOL=0.00001):
    H = get_jacobi_H(mat, n)
    G = get_jacobi_G(mat, n)
    k = 1
    print("Jacobi:")
    print("Iteration" + "\t\t\t".join(
        [" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(mat) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")
    while True:
        x = np.dot(G, X0) + np.dot(H, b)
        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))
        if norm(x - X0, np.inf) < TOL:
            return tuple(x)
        k += 1
        X0 = x.copy()


def get_jacobi_solution(mat, b, n, X0):
    if check_if_singular(mat, b, n) == -1:
        if not is_diagonally_dominant(mat):
            print('Matrix is not diagonally dominant!\n')
        else:
            return jacobi_iterative(mat, b, n, X0)

