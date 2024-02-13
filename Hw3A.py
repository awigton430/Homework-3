
def AaugMatrix():  # Function reused from HW 2
    """
        Creates an augmented matrix of n rows and n + columns.

        Args:
        - none

        Returns:
        Aaug: Augmented matrix
        """
    n = int(input("Enter the number of rows: "))
    Aaug = []
    for i in range(n):
        row = []
        for j in range(n):
            element = float(input(f"Enter element for row {i + 1}, column {j + 1}: "))
            row.append(element)
        # Append the right-hand side value for each equation
        b = float(input(f"Enter the value for the right-hand side of equation {i + 1}: "))
        row.append(b)
        Aaug.append(row)
    return Aaug

def isSymmetric(Aaug, n):  # Chat GPT was used to fix errors
    """
        Checks if a matrix is symmetric.

        Args:
        - Aaug (list): List of lists representing the matrix.
        - n (int): The number of rows in the matrix.

        Returns:
        print: Prints whether matrix is symmetric or not
        """
    for i in range(n - 1):
        if Aaug[i][i+1] != Aaug[i+1][i]:
            print("Matrix is not symmetric")
            return False
    print("Matrix is symmetric")

def isDiagDominant(Aaug, n): # Chat GPT was used to fix errors
    """
        Checks if a matrix is diagonally dominant.

        Args:
        - Aaug (list): List of lists representing the matrix.
        - n (int): The number of rows in the matrix.

        Returns:
        print: Prints whether matrix is diagonally dominant or not
        """
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += abs(Aaug[i][j])
        if abs(Aaug[i][i]) <= row_sum:
            print("Matrix is not diagonally dominant.")
            return False
    print("Matrix is diagonally dominant.")

def cholesky(Aaug, n): # Chat GPT was used help construct this function
    """
        Solves an augmented matrix by Cholesky decomposition.

        Args:
        - Aaug (list): List of lists representing the matrix.
        - n (int): The number of rows in the matrix.

        Returns:
        L: Decomposed lower triangular matrix
        """
    L = [[0] * n for i in range(n)]  # Empty lower triangular matrix
    for i in range(n):
        for j in range(i+1):
            if i == j:  # Calculates diagonal elements according to Cholesky's Method formula
                sumTerm = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = (Aaug[i][i] - sumTerm) ** 0.5
            else:  # Calculates non-diagonal elements according to Cholesky's Method formula
                sumTerm = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (Aaug[i][j] - sumTerm) / L[j][j]
    return L

def doolittle(Aaug, n):  # Chat GPT was used help construct this function
    """
        Solves an augmented matrix by Doolittle's decomposition.

        Args:
        - Aaug (list): List of lists representing the matrix.
        - n (int): The number of rows in the matrix.

        Returns:
        L: Decomposed lower triangular matrix
        U: Decomposed upper triangular matrix
        """
    L = [[0] * n for i in range(n)]  # Empty lower triangular matrix
    U = [[0] * n for i in range(n)]  # Empty upper triangular matrix
    for k in range(n):  # Columns 'k'
        for j in range(k, n):  # Calculates upper triangular matrix according to Doolittle's Method formula
            U[k][j] = Aaug[k][j] - sum(L[k][i] * U[i][j] for i in range(k))

        for i in range(k + 1, n):  # Calculates lower triangular matrix according to Doolittle's Method formula
            L[i][k] = (Aaug[i][k] - sum(L[i][m] * U[m][k] for m in range(k))) / U[k][k]
    return L, U

def main():
    """
        Calls functions and shows the results of Cholesky or Doolittle decomposition

        Args:
        - none

        Returns:
        print: Prints the results of Cholesky or Doolitle method
        """
    matrix = AaugMatrix()
    n = len(matrix)
    if isSymmetric(matrix, n):
        if isDiagDominant(matrix, n):
            print("Cholesky's Method:")
            print(cholesky(matrix, n))
    else:
        print("Doolittle's Method:")
        print(doolittle(matrix, n))

main()



