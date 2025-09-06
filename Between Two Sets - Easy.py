#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    len_a = len(a)
    len_b = len(b)
    count = 0

    for i in range(len_a):
        print(a[i]*(i+1))

# print(getTotalX([2,4],[16,32,96])) # 3
print(getTotalX([4],[24,36])) # 2


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     arr = list(map(int, input().rstrip().split()))

#     brr = list(map(int, input().rstrip().split()))

#     total = getTotalX(arr, brr)

#     fptr.write(str(total) + '\n')

#     fptr.close()
