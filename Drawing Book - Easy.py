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
    res_start = 0
    res_end = 0
    
    for i in range(0,p):
        ctr_start += 1
        # if p == i:
        #     ctr += 1

    for k in range(n,p,-1):
        ctr_end += 1
    
    res_start = abs(int((n/p)-ctr_start))

    if ctr_end%2 == 0:
        res_end = abs(int((n/p)-ctr_end-1))
    else:
        res_end = abs(int((n/p)-ctr_end))
    

    if res_start < res_end:
        return res_start
    else:
        return res_end


    
    # return abs(ctr_start-p), abs(ctr_end-p)
    # return ctr_start, ctr_end
    # return abs(int((n/p)-ctr_start)), abs(int((n/p)-ctr_end))

print(pageCount(6,2)) #1 #2
print(pageCount(5,4)) #2 #0
print(pageCount(5,3)) 
print(pageCount(2,1)) 


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     p = int(input().strip())

#     result = pageCount(n, p)

#     fptr.write(str(result) + '\n')

#     fptr.close()
