#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arr_len = len(arr)
    pos = 0
    neg = 0
    null = 0

    for i in range(arr_len):
        if arr[i] > 0: # pos
            pos += 1
        if arr[i] < 0: # min
            neg += 1
        if arr[i] == 0:
            null += 1
    
    # return pos/arr_len, neg/arr_len, min/arr_len
    # return f"{pos/arr_len:.6f}\n{neg/arr_len:.6f}\n{null/arr_len:.6f}"
    print(f"{pos/arr_len:.6f}")
    print(f"{neg/arr_len:.6f}")
    print(f"{null/arr_len:.6f}")

# print(plusMinus([-4, 3, -9, 0, 4, 1]))
plusMinus([-4, 3, -9, 0, 4, 1])
# test


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)
