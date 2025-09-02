#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = 0
    count_orange = 0

    len_apple = len(apples)
    len_orange = len(oranges)

    for i in range(len_apple):
        if a + apples[i] >= s and a + apples[i] <= t:
            count_apple += 1
    
    for k in range(len_orange):
        if b + oranges[k] >= s and b + oranges[k] <= t:
            count_orange += 1
    
    # return count_apple, count_orange
    print(count_apple)
    print(count_orange)

# print(countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4]))



# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     s = int(first_multiple_input[0])

#     t = int(first_multiple_input[1])

#     second_multiple_input = input().rstrip().split()

#     a = int(second_multiple_input[0])

#     b = int(second_multiple_input[1])

#     third_multiple_input = input().rstrip().split()

#     m = int(third_multiple_input[0])

#     n = int(third_multiple_input[1])

#     apples = list(map(int, input().rstrip().split()))

#     oranges = list(map(int, input().rstrip().split()))

#     countApplesAndOranges(s, t, a, b, apples, oranges)
