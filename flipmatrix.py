def flipMatrix(matrix):
  """
  Finds the maximum sum achievable by flipping hourglass-shaped submatrices.

  Args:
      matrix: A 2D list of integers representing the matrix.

  Returns:
      The maximum sum achievable by flipping submatrices (integer).
  """

  n = len(matrix)
  max_sum = 0

  # Iterate through all possible submatrices (excluding corners)
  for i in range(1, n - 1):
    for j in range(1, n - 1):
      # Calculate potential sum with flipped submatrix
      flipped_sum = matrix[i][j] + matrix[i][n - 1 - j] + matrix[i - 1][j] + matrix[i - 1][n - 1 - j] + matrix[n - 1 - i][j] + matrix[n - 1 - i][n - 1 - j]

      # Compare with original submatrix sum and update max_sum
      original_sum = matrix[i][j] + matrix[i][n - 1 - j] + matrix[i - 1][j] + matrix[i - 1][n - 1 - j]
      max_sum += max(flipped_sum, original_sum)

  print(max_sum)

# Example usage:
matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]

flipped_matrix = flipMatrix(matrix)
