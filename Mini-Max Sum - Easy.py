#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sort_arr(arr):
    arr_len = len(arr)

    for i in range(arr_len):
        for k in range(arr_len-1): # supaya ga out of index
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    
    return arr


def miniMaxSum(arr):
    sort_arr(arr)
    arr_len = len(arr)
    sum_arr = 0

    for num in arr:
        sum_arr += num
    
    min_res = sum_arr-arr[arr_len-1]
    max_res = sum_arr-arr[0]
        
    print(min_res, max_res)

miniMaxSum([5,2,3,4,1])
# print(sort_arr([5,1,2,3,4]))
        


# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)
