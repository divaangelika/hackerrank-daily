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
        # for i in range(n):
            # while()
        print(" " * (n-k-1) + "#" * (k+1))
        # print("#" * (k+1) + " " * (n-1))
        # print()
            
staircase(10)
    

# if __name__ == '__main__':
#     n = int(input().strip())

#     staircase(n)