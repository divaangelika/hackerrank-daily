#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    s_len = len(s)
    sum_temp = 0
    sum_arr = []
    count = 0
    y = 0

    # if s_len == 1 and s[0] == d and m == 1:
    #     return count+1

    if m == 1 and s_len == 1:
        if d > s[0] or d < s[0]:
            return 0
        elif d == s[0]:
            return 1
    else:       
        for i in range(s_len-m+1):
            sum_temp = 0
            for k in range(i, i+m):
                sum_temp += s[k]
                # sum_arr.append(s[k])
                # print("index",i,",",s[k])
                # total = s[k]+s[m+i-1]
                # print(s[k],"+",s[m+i-1],"=",total)

            if sum_temp == d:
                count += 1

    # return sum_arr, count
    # return sum_arr, sum_temp, count
    # return sum_arr, sum_temp
    return count

print(birthday([1,2,1,3,2],3,2)) #2
print(birthday([1,1,1,1,1,1],3,2)) #0
print(birthday([1,2],2,2)) #0
print(birthday([4],4,1)) #1
            

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     s = list(map(int, input().rstrip().split()))

#     first_multiple_input = input().rstrip().split()

#     d = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     result = birthday(s, d, m)

#     fptr.write(str(result) + '\n')

#     fptr.close()
