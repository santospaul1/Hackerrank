def diagonalDifference(arr):
  """
  Calculates the absolute difference between the sums of diagonals in a square matrix.

  Args:
      arr: A square matrix represented as a list of lists of integers.

  Returns:
      The absolute difference between the sums of diagonals.
  """

  n = len(arr)  # Get the size of the square matrix
  primary_sum = 0
  secondary_sum = 0

  for i in range(n):
    primary_sum += arr[i][i]  # Add elements on the primary diagonal
    secondary_sum += arr[i][n - 1 - i]  # Add elements on the secondary diagonal

  return abs(primary_sum - secondary_sum)  # Return absolute difference

# Example usage
matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
difference = diagonalDifference(matrix)
print(difference)  # Output: 15
