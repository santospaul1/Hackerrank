def staircase(n):
  """
  Prints a right-aligned staircase of size n using # symbols and spaces.

  Args:
      n: The size of the staircase (height and width).
  """

  # Iterate for each row (from 0 to n-1)
  for i in range(n):
    # Calculate the number of spaces to print for right-alignment
    spaces = n - i - 1
    # Print the spaces
    print(' ' * spaces, end='')
    # Print the # symbols for the current row
    print('#' * (i + 1))

if __name__ == '__main__':
  n = int(input())
  staircase(n)
