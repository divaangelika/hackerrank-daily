#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    ctr_start = 0
    ctr_end = 0
    ctr_p = 0
    ctr_n = 0

    if p == 1:
        return 0
    else:
        ctr_start = int(p/2)
        ctr_p = int(p/2)
        ctr_n = int(n/2)
        ctr_end = ctr_n - ctr_p

        if ctr_start < ctr_end:
            return ctr_start
        else:
            return ctr_end

# print(pageCount(6,2)) #1 #2
# print(pageCount(5,4)) #2 #0
# print(pageCount(5,3)) 
# print(pageCount(2,1)) 
# print(pageCount(1,1)) 
# print(pageCount(10,2)) 
print(pageCount(7,4)) 


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     p = int(input().strip())

#     result = pageCount(n, p)

#     fptr.write(str(result) + '\n')

#     fptr.close()
