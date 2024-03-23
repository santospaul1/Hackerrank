#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    x = len(s)
    found = []
    for char in range(x):
        if s[char] != s[char - 1] and s[char] != s[char -2]:
            return char
        return -1
    
    

#s = 'aaab'
#s = 'baa'
s = 'aaa'
print(palindromeIndex(s))    
    # Write your code here
