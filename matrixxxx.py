def input_matrix(rows, cols):
    """Input a matrix with given rows and columns."""
    print(f"Input matrix {rows}x{cols}:")
    return [[float(input(f"Element [{i+1},{j+1}]: ")) for j in range(cols)] for i in range(rows)]

def display_matrix(matrix):
    """Display a matrix."""
    for row in matrix:
        print("\t".join(map(str, row)))

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for col in range(len(matrix)):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is not invertible.")
    size = len(matrix)
    adjoint = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            sub_matrix = [row[:j] + row[j+1:] for idx, row in enumerate(matrix) if idx != i]
            adjoint[j][i] = ((-1) ** (i + j)) * determinant(sub_matrix)
    return [[adjoint[i][j] / det for j in range(size)] for i in range(size)]

def main():
    print("Matrix Operations (Max 4x4)")
    while True:
        print("\nOptions:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Determinant")
        print("5. Inverse")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            rows, cols = map(int, input("Enter dimensions (rows cols): ").split())
            matrix1 = input_matrix(rows, cols)
            matrix2 = input_matrix(rows, cols)
            result = add_matrices(matrix1, matrix2)
            print("Result:")
            display_matrix(result)

        elif choice == "2":
            rows, cols = map(int, input("Enter dimensions (rows cols): ").split())
            matrix1 = input_matrix(rows, cols)
            matrix2 = input_matrix(rows, cols)
            result = subtract_matrices(matrix1, matrix2)
            print("Result:")
            display_matrix(result)

        elif choice == "3":
            rows1, cols1 = map(int, input("Enter dimensions of first matrix (rows cols): ").split())
            matrix1 = input_matrix(rows1, cols1)
            rows2, cols2 = map(int, input("Enter dimensions of second matrix (rows cols): ").split())
            if cols1 != rows2:
                print("Matrix multiplication not possible.")
                continue
            matrix2 = input_matrix(rows2, cols2)
            result = multiply_matrices(matrix1, matrix2)
            print("Result:")
            display_matrix(result)

        elif choice == "4":
            size = int(input("Enter size of square matrix (2-4): "))
            if size < 2 or size > 4:
                print("Invalid size.")
                continue
            matrix = input_matrix(size, size)
            det = determinant(matrix)
            print(f"Determinant: {det}")

        elif choice == "5":
            size = int(input("Enter size of square matrix (2-4): "))
            if size < 2 or size > 4:
                print("Invalid size.")
                continue
            matrix = input_matrix(size, size)
            try:
                inv = inverse(matrix)
                print("Inverse:")
                display_matrix(inv)
            except ValueError as e:
                print(e)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
