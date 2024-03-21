def findZigZagSequence(a, n):
    """
    Finds the lexicographically smallest zig zag sequence for a given array.

    Args:
        a: A list of distinct integers representing the input array.
        n: The length of the list (number of elements).

    Returns:
        None (prints the zig zag sequence directly).
    """

    # Sort the array in ascending order
    a.sort()

    # Swap the middle element with the last element for base case
    mid = (n + 1) // 2
    a[mid], a[n - 1] = a[n - 1], a[mid]

    # Create two pointers for zig-zagging
    st = mid + 1
    ed = n - 2

    # Iterate while pointers haven't crossed each other
    while st <= ed:
        # Swap elements at st and ed for zig-zag pattern
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1

    # Print the zig-zag sequence
    for num in a:
        print(num, end=" ")

    print()  # Add a newline after each test case

# Get the number of test cases
a = [1, 2, 3, 4, 7, 6, 5]
n = len(a)
(findZigZagSequence(a, n))
