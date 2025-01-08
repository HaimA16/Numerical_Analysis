import sympy as sp


from sympy.utilities.lambdify import lambdify
from math import isclose

from Numerical_Analysis.HW2.Bisection_Method import bisection_method_with_interval
from Numerical_Analysis.HW2.secant_method import secant_method_with_interval
from Numerical_Analysis.HW2.Newton_Raphson import newton_raphson_with_interval
def main():

    x = sp.symbols('x')
    polynomial = sp.Poly(input("Enter the polynomial: "), x).as_expr()
    start_point = float(input("Enter the start of the interval: "))
    end_point = float(input("Enter the end of the interval: "))

    subinterval_size = float(input("Enter the subinterval size (e.g., 0.1): "))

    print("\nChoose a method to find the roots:")
    print("1. Bisection Method")
    print("2. Newton-Raphson Method")
    print("3. Secant Method")
    method_choice = int(input("Enter your choice (1, 2, or 3): "))

    f = lambdify(x, polynomial)
    f_derivative = lambdify(x, sp.diff(polynomial, x))

    roots = []
    current_start = start_point
    while current_start < end_point:
        current_end = current_start + subinterval_size
        if current_end > end_point:
            current_end = end_point

        if f(current_start) * f(current_end) <= 0 or isclose(f(current_start), 0) or isclose(f(current_end), 0):
            try:
                if method_choice == 1:

                    root = bisection_method_with_interval(polynomial, current_start, current_end, epsilon=1e-6)
                    print(f"Bisection Method: Root found at x = {root:.6f}")
                elif method_choice == 2:

                    root = newton_raphson_with_interval(polynomial, (current_start + current_end) / 2, current_end, epsilon=1e-6)
                    print(f"Newton-Raphson Method: Root found at x = {root:.6f}")
                elif method_choice == 3:

                    root = secant_method_with_interval(polynomial, current_start, current_end, epsilon=1e-6)
                    print(f"Secant Method: Root found at x = {root:.6f}")
                else:
                    print("Invalid choice.")
                    return


                if not any(isclose(root, r, abs_tol=1e-6) for r in roots):
                    roots.append(root)

            except Exception as e:
                print(f"Error in finding root in interval [{current_start}, {current_end}]: {e}")

        current_start += subinterval_size

    print(f"\nAll roots found: {sorted(roots)}")


if __name__ == "__main__":
    main()
