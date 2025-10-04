#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    flag = 0
    arr_path = []

    for i in range(len(path)):
        if i == 1 or i == 2 and path[i] == 'D':
            continue
        elif path[i] == 'D':
            arr_path.append(path[i])
            # if arr_path[0] 
        elif path[i] == 'U':
            if arr_path[0] == 'D':
                flag += 1

    return flag

print(countingValleys("8","UDDDUDUU"))

    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     steps = int(input().strip())

#     path = input()

#     result = countingValleys(steps, path)

#     fptr.write(str(result) + '\n')

#     fptr.close()
