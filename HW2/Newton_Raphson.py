import sympy as sp
from sympy.utilities.lambdify import lambdify


def newton_raphson_with_interval(polynomial, start_point, end_point, epsilon=0.0001, max_iter=50):

    x = sp.symbols('x')

    f = lambdify(x, polynomial)
    df = lambdify(x, sp.diff(polynomial, x))

    p0 = (start_point + end_point) / 2

    print("{:<10} {:<15} {:<15}".format("Iteration", "p0", "p1"))

    for i in range(1, max_iter + 1):
        if df(p0) == 0:
            raise ValueError("Derivative is zero at p0, method cannot continue.")

        p1 = p0 - f(p0) / df(p0)
        error = abs(p1 - p0)

        print("{:<10} {:<15.9f} {:<15.9f}".format(i, p0, p1))
        if error < epsilon:
            print(f"Root found after {i} iterations.")
            return p1

        p0 = p1

        if p1 < start_point or p1 > end_point:
            raise ValueError("The root is outside the specified interval.")

    raise RuntimeError(f"Method did not converge after {max_iter} iterations.")
