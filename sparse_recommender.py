class SparseMatrix:
    def __init__(self, rows, cols):
        # Create an empty data structure (dictionary) to store non-zero elements
        self.rows = rows  # The number of rows in the matrix
        self.cols = cols  # The number of columns in the matrix
        self.matrix = {}  # Store the matrix elements in a dictionary

    def set(self, row, col, value):
        # Set a value at a specific position (row, column) in the matrix
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[(row, col)] = value
        else:
            raise ValueError("Row and column indices must be within a valid range.")

    def get(self, row, col):
        # Get the value at a specific position (row, column) in the matrix
        if (row, col) in self.matrix:
            return self.matrix[(row, col)]
        else:
            # If the element is not in the dictionary, assume its value is 0 (sparse matrix assumption)
            return 0

    def recommend(self, user_vector):
        # Recommend items to a user based on a user vector
        if len(user_vector) != self.cols:
            raise ValueError("User vector size must match the number of columns in the matrix.")

        # Initialize a result vector with zeros
        result_vector = [0] * self.rows

        # Multiply the matrix with the user vector to make recommendations
        for (row, col), value in self.matrix.items():
            result_vector[row] += value * user_vector[col]

        return result_vector

    def add_movie(self, other_matrix):
        # Add another matrix to the current matrix
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrix dimensions must be the same for addition.")
        
        # Check for negative values in the matrices
        if any(value < 0 for value in self.matrix.values()) or any(value < 0 for value in other_matrix.matrix.values()):
            raise ValueError("Matrices cannot contain negative values.")

        # Create a new matrix to store the result
        result_matrix = SparseMatrix(self.rows, self.cols)

        # Copy the values from the current matrix to the result matrix
        for (row, col), value in self.matrix.items():
            result_matrix.set(row, col, value)

        # Add the values from the other matrix to the result matrix
        for (row, col), value in other_matrix.matrix.items():
            result_matrix.set(row, col, result_matrix.get(row, col) + value)

        return result_matrix


    def to_dense(self):
        # Convert the matrix to a regular 2D list (matrix) filled with zeros
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]

        # Fill in the non-zero elements from the dictionary into the dense matrix
        for (row, col), value in self.matrix.items():
            dense_matrix[row][col] = value

        return dense_matrix
