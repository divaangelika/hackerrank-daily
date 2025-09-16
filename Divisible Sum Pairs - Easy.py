#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    ctr = 0
    
    for i in range(n-1):
        for j in range(n-1):
            # if ar[i] < ar[j+1]:
            if i < j+1:
                sum_temp = 0
                sum_temp = ar[i] + ar[j+1]

                if sum_temp % k == 0:
                    ctr += 1

    return ctr

# print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))
# print(divisibleSumPairs(6,5,[1,2,3,4,5,6]))



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     ar = list(map(int, input().rstrip().split()))

#     result = divisibleSumPairs(n, k, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
