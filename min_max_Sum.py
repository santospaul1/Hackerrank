#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    x = sorted(arr)
    maximum = []
    minimum = []
    n = len(arr)
    for i in range(0, n-1):
        minimum.append(x[i])
    for j in range(1, n):
        maximum.append(x[j])
    print(sum(minimum), sum(maximum))
        
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
