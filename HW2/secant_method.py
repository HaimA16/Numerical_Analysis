import sympy as sp
from sympy.utilities.lambdify import lambdify

def secant_method_with_interval(polynomial, start_point, end_point, epsilon=0.0001, max_iter=50):

    x = sp.symbols('x')
    f = lambdify(x, polynomial)

    x0, x1 = start_point, end_point
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "x0", "x1", "p"))

    for i in range(1, max_iter + 1):
        if f(x1) - f(x0) == 0:
            raise ValueError("Denominator becomes zero; the method cannot continue.")

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))
        error = abs(p - x1)

        print("{:<10} {:<15.9f} {:<15.9f} {:<15.9f}".format(i, x0, x1, p))

        if error < epsilon:
            print(f"Root found after {i} iterations.")
            return p

        x0, x1 = x1, p

    raise RuntimeError(f"Method did not converge after {max_iter} iterations.")
