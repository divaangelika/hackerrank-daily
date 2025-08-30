#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def sort_arr(candles):
    candles_len = len(candles)
    
    for i in range(candles_len):
        for k in range(candles_len-1):
            if candles[k] > candles[k+1]:
                temp = candles[k+1]
                candles[k+1] = candles[k]
                candles[k] = temp
    
    return candles

def birthdayCakeCandles(candles):
    candles_sorted = sort_arr(candles)
    len_sorted_candles = len(candles_sorted)
    max_height_candles = candles_sorted[len_sorted_candles-1]
    res = 1

    for i in range(len_sorted_candles-1):
        if candles_sorted[i] == max_height_candles:
            res += 1
    
    # print(candles_sorted[len_sorted_candles-1])
    return res

# print(birthdayCakeCandles([3,2,1,3]))
# print(birthdayCakeCandles([3,1,2]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()