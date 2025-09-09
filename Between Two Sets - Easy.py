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
    count = 0
    # kelipatan_a = []
    # kelipatan_b = []

    max_a = a[0]
    for num in a:
        if num > max_a:
            max_a = num
    
    min_b = b[0]
    for num in b:
        if num < min_b:
            min_b = num

    # for i in a:
    #     for k in range(1,10):
    #         kelipatan_a.append(i*k)
    #     # return kelipatan_a

    # for i in b:
    #     for k in range(1,10):
    #         kelipatan_b.append(i*k)
    
    # for j in kelipatan_a:
    #     if j in kelipatan_b:
    #         count += 1

    for x in range(max_a, min_b+1):
        valid = True

        for ai in a:
            if x % ai != 0:
                valid = False
                break
        
        if valid == True:
            for bi in b:
                if bi % x != 0:
                    valid = False
                    break

        if valid == True:
            count += 1


    return count

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
