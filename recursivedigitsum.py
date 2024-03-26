#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    
    concatenated_n = n * k
    
    # Calculate the sum of digits of the concatenated string
    digit_sum = sum(int(digit) for digit in concatenated_n)
    
    # If the sum has more than one digit, calculate the super digit recursively
    while digit_sum >= 10:
        digit_sum = sum(int(digit) for digit in str(digit_sum))
    
    return digit_sum
  # Recursively calculate the super digit of the digit sum
    #return superDigit(str(digit_sum), 1)

    
    
                

     
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
