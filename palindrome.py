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
    if s == s[::-1]:
       return -1

  # Find the first mismatching character from left and right ends
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
      # Check removing left or right character makes a palindrome
            if s[left + 1:right + 1] == s[left + 1:right + 1][::-1]:
                return left
            else:
                return right
            left += 1
            right -= 1

  # No removable character found
    return -1

            
        
    
    

s = 'aaab'
t = 'baa'
u = 'aaa'
print(palindromeIndex(s))  
print(palindromeIndex(t))   
print(palindromeIndex(u)) 
    # Write your code here
