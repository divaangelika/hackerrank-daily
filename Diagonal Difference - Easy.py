#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    arr_len = len(arr)
    res_left = 0
    res_right = 0

    for i in range(arr_len):
        for j in range(arr_len):
            if i == j:
                res_left += arr[i][j]
            if i + j == arr_len-1:
                res_right += arr[i][j]
    
    return abs(res_left - res_right)

# print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
