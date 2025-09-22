#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    arr_len = len(arr)
    # print(arr)
    count_cont = []
    flag = []
    max_arr = 0 #2
    res = 0

    for i in range(1,6):
        count = 0
        for k in range(arr_len):
            if arr[k] == i:
                count += 1
        
        count_cont.append(count)
    
    arr_count = len(count_cont) 
    # print(arr_count) 
    for j in range(arr_count): 
        if count_cont[j] > max_arr: 
            # max_arr = j
            max_arr = count_cont[j]
        
    for k in range(arr_count):
        if max_arr == count_cont[k]:
            res == k


    # return max_arr, count_cont
    return max_arr, res, count_cont
    # return arr_count, count_cont
    # return max_arr

print(migratoryBirds([1,4,4,4,5,3]))
print(migratoryBirds([1,2,3,4,5,4,3,2,1,3,4]))
print(migratoryBirds([1,1,2,2,3]))

    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
