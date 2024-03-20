def timeConversion(s):
  """
  Converts a time in 12-hour AM/PM format to 24-hour format.

  Args:
      s: A string representing the time in 12-hour AM/PM format.

  Returns:
      A string representing the time in 24-hour format.
  """

  # Extract hours, minutes, seconds, and meridian
  hours, minutes, seconds = map(int, s[:-2].split(':'))
  meridian = s[-2:]

  # Convert to 24-hour format
  if meridian == 'PM' and hours != 12:
    hours += 12
  elif meridian == 'AM' and hours == 12:
    hours = 0

  return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Example usage
time = "07:05:45PM"
converted_time = timeConversion(time)
print(converted_time)  # Output: 19:05:45
