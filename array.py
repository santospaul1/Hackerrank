def countingSort(arr):
  """
  Sorts a list of integers using counting sort and returns the frequency array.

  Args:
      arr: A list of integers.

  Returns:
      A list of integers representing the frequency of each value (0-99).
  """

  # Create a frequency array to store the count of each value (0-99)
  count_arr = [0] * 100

  # Count the occurrences of each element in the input array
  for num in arr:
    count_arr[num] += 1

  return count_arr

# Example usage
arr = [63, 25, 73, 1, 98,]  # Sample input from prompt
frequency_arr = countingSort(arr)
print(frequency_arr)