def lonelyinteger(a):
  """
  Finds the unique element in an array where all other elements occur twice.

  Args:
      a: A list of integers.

  Returns:
      The unique integer in the list.
  """

  # Use XOR (exclusive OR) to find the unique element
  result = 0
  for num in a:
    result ^= num  # XOR each element with the result

  return result

# Example usage
arr = [1, 2, 3, 4, 3, 2, 4]
unique = lonelyinteger(arr)
print(unique)  # Output: 1
