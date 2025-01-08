import numpy as np
import sympy as sp
from sympy.utilities.lambdify import lambdify

def bisection_method_with_interval(polynomial, start_point, end_point, epsilon=0.0001):
    x = sp.symbols('x')
    f = lambdify(x, polynomial)

    if np.sign(f(start_point)) == np.sign(f(end_point)):
        raise ValueError("The scalars start_point and end_point do not bound a root.")

    a, b = start_point, end_point
    c = a
    iterations = 0

    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "c", "Error"))

    while abs(b - a) > epsilon:
        iterations += 1
        c_prev = c
        c = (a + b) / 2
        error = abs(c - c_prev)

        print("{:<10} {:<15.9f} {:<15.9f} {:<15.9f} {:<15.9f}".format(iterations, a, b, c, error))

        if abs(f(c)) < epsilon or error < epsilon:
            print(f"Root found after {iterations} iterations.")
            return c

        if np.sign(f(a)) == np.sign(f(c)):
            a = c
        else:
            b = c

    raise RuntimeError(f"Method did not converge after {iterations} iterations.")
