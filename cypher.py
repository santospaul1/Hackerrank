#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encrypted = ""
    for char in s:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            # Encrypt the character by shifting it by k positions
            encrypted += chr((ord(char) - base + k) % 26 + base)
        else:
            # If the character is not a letter, keep it unchanged
            encrypted += char
    return encrypted
    # Write your code here

s = 'middle-Outz'
k = 2
print(caesarCipher(s, k))