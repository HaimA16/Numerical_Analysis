import copy


def is_matrix_diagonally_dominant(matrix):
    """
    Checks if a matrix is diagonally dominant.
    This means the number on the diagonal is bigger than
    the sum of other numbers in the same row.

    Args:
      matrix: A list of lists (a matrix).

    Returns:
      True if diagonally dominant, False if not.
    """
    n = len(matrix)
    for i in range(n):
        diagonal = abs(matrix[i][i])  # Get the diagonal number
        row_sum = 0
        for j in range(n):
            if i != j:
                row_sum += abs(matrix[i][j])  # Add other numbers in the row
        if diagonal <= row_sum:
            return False  # Not diagonally dominant
    return True  # It is diagonally dominant


def try_to_rearrange_matrix_rows(matrix, vector):
    """
    Tries to swap rows to make the matrix diagonally dominant.

    Args:
      matrix: A list of lists (a matrix).
      vector: A list (the vector).

    Returns:
      The rearranged matrix and vector, or the original ones if it can't be done.
    """
    n = len(matrix)
    new_matrix = copy.deepcopy(matrix)  # Copy the matrix so we don't change the original
    new_vector = copy.deepcopy(vector)  # Copy the vector

    for i in range(n):
        biggest_row = i
        for k in range(i + 1, n):
            if abs(new_matrix[k][i]) > abs(new_matrix[biggest_row][i]):
                biggest_row = k

        # Swap rows in matrix
        new_matrix[i], new_matrix[biggest_row] = new_matrix[biggest_row], new_matrix[i]
        # Swap elements in vector
        new_vector[i], new_vector[biggest_row] = new_vector[biggest_row], new_vector[i]

    if is_matrix_diagonally_dominant(new_matrix):
        return new_matrix, new_vector
    else:
        return matrix, vector


def solve_jacobi_method(matrix, vector, tolerance=0.00001, max_iterations=100):
    """
    Solves a system of linear equations using Jacobi method.

    Args:
      matrix: A list of lists (a matrix).
      vector: A list (the vector).
      tolerance: How close the solution needs to be.
      max_iterations: Max number of tries.

    Returns:
      The solution, number of tries, and a message.
    """
    n = len(matrix)
    x = [0.0] * n  # Start with a guess of 0 for all
    iterations = 0
    converged = False
    message = ""

    for _ in range(max_iterations):
        x_new = [0.0] * n  # New guess
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += matrix[i][j] * x[j]
            x_new[i] = (vector[i][0] - s) / matrix[i][i]

        print(f"Try {iterations + 1}: {x_new}")

        # Check if the new guess is close enough to the previous one
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            converged = True
            message = "Solution found!"
            break

        x = x_new[:]  # Update the guess
        iterations += 1

    if not converged:
        message = f"Not solved after {max_iterations} tries."

    return x, iterations, message


def solve_gauss_seidel_method(matrix, vector, tolerance=0.00001, max_iterations=100):
    """
    Solves a system of linear equations using Gauss-Seidel method.

    Args:
      matrix: A list of lists (a matrix).
      vector: A list (the vector).
      tolerance: How close the solution needs to be.
      max_iterations: Max number of tries.

    Returns:
      The solution, number of tries, and a message.
    """
    n = len(matrix)
    x = [0.0] * n  # Start with a guess of 0 for all
    iterations = 0
    converged = False
    message = ""

    for _ in range(max_iterations):
        x_old = x[:]  # Remember the old guess
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += matrix[i][j] * x[j]
            x[i] = (vector[i][0] - s) / matrix[i][i]

        print(f"Try {iterations + 1}: {x}")

        # Check if solution is close enough to the old one
        if all(abs(x[i] - x_old[i]) < tolerance for i in range(n)):
            converged = True
            message = "Solution found!"
            break

        iterations += 1

    if not converged:
        message = f"Not solved after {max_iterations} tries."

    return x, iterations, message


def solve_system(matrix, vector, method):
    """
    Solves a system of equations.
    Checks if diagonally dominant, rearranges if needed, then solves.

    Args:
      matrix: A list of lists (a matrix).
      vector: A list (the vector).
      method: "jacobi" or "gauss_seidel".

    Returns:
      The solution, number of tries, and a message.
    """
    original_matrix = copy.deepcopy(matrix)  # copy original matrix
    original_vector = copy.deepcopy(vector)  # copy original vector

    # Check if diagonally dominant
    if not is_matrix_diagonally_dominant(matrix):
        print("Matrix is not diagonally dominant. Trying to rearrange.")
        matrix, vector = try_to_rearrange_matrix_rows(matrix, vector)
        if not is_matrix_diagonally_dominant(matrix):
            print("Still not diagonally dominant. Trying anyway.")

            # Try to solve even if not diagonally dominant
            if method == "jacobi":
                x, iterations, message = solve_jacobi_method(matrix, vector)
            else:
                x, iterations, message = solve_gauss_seidel_method(matrix, vector)

            if "Solution found!" in message:
                return x, iterations, "It worked, even without diagonal dominance. Results: " + str(x)
            else:
                return x, iterations, "System didn't converge"

    # Solve using the chosen method
    if method == "jacobi":
        x, iterations, message = solve_jacobi_method(matrix, vector)
    elif method == "gauss_seidel":
        x, iterations, message = solve_gauss_seidel_method(matrix, vector)
    else:
        return None, 0, "Wrong method chosen. Use 'jacobi' or 'gauss_seidel'."

    return x, iterations, message


# --- Main Program ---
matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
vectorB = [[2], [6], [5]]

method_choice = input("Choose a method (jacobi or gauss_seidel): ")

if method_choice.lower() in ("jacobi", "gauss_seidel"):
    solution, num_iterations, msg = solve_system(matrixA, vectorB, method_choice.lower())
    print(f"\nSolution: {solution}")
    print(f"Number of tries: {num_iterations}")
    print(msg)
else:
    print("Wrong method chosen.")