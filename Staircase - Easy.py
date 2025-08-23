#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for k in range(n):
        for i in range(n-1,-1,-1):
            # print("#", end="")
            # if i == n-1:
            #     print("#", end="")
            
            while(i<k and i<0):
                print("#", end="")
                break
            if i == k:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    # print()

staircase(10)
    

# if __name__ == '__main__':
#     n = int(input().strip())

#     staircase(n)