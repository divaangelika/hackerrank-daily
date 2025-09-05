#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    if (x1 < x2 and v1 <= v2) or (x2 > x1 and v2 >= v1):
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"


    # x1_var = x1
    # v1_var = v1
    # x2_var = x2
    # v2_var = v2

    # while True:
    #     if 

print(kangaroo(0,2,5,3))  # YES
print(kangaroo(0,3,4,2))  # YES
print(kangaroo(2,1,1,2))  # NO
print(kangaroo(1,2,1,1))  # NO

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     x1 = int(first_multiple_input[0])

#     v1 = int(first_multiple_input[1])

#     x2 = int(first_multiple_input[2])

#     v2 = int(first_multiple_input[3])

#     result = kangaroo(x1, v1, x2, v2)

#     fptr.write(result + '\n')

#     fptr.close()
