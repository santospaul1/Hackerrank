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
    n = len(s)
    
    for i in range(n):
        if s[i] != s[i-1] and s[i] != s[i-2]:
            return i
    return -1

  # Find the first mismatching character from left and right ends
    

  # No removable character found
    

            
        
    
    

s = 'aaab'
t = 'baa'
u = 'aaa'
x = 'aaaac'
print(palindromeIndex(s))  
print(palindromeIndex(t))   
print(palindromeIndex(u)) 
print(palindromeIndex(x)) 

    # Write your code here
