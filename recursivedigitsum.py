def superDigit(n, k):
    # Calculate the super digit of a number
    def calculate_super_digit(num):
        # If the number has only one digit, return that digit
        if len(num) == 1:
            return int(num)
        # Otherwise, sum the digits and recursively calculate the super digit
        else:
            digit_sum = sum(int(digit) for digit in num)
            return calculate_super_digit(str(digit_sum))

    # Concatenate n k times and calculate the super digit
    concatenated_n = n * k
    return calculate_super_digit(concatenated_n)



n = '1111'
k = 4
print(superDigit(n,k))