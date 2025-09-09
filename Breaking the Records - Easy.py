#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    scores_len = len(scores)
    arr_max = []
    arr_min = []
    max_res = 0
    min_res = 0
    temp_max  = scores[0]
    temp_min = scores[0]

    for i in range(1, scores_len):
        if scores[i] < temp_min:
            temp_min = scores[i]
            arr_min.append(scores[i])
        elif scores[i] > temp_max:
            temp_max = scores[i]
            arr_max.append(scores[i])

    # if scores[0] > scores[1]:
    #     min_res += 1
    #     arr_min.append(scores[1])

    #     for i in range(1,scores_len-1):
    #         if scores[i] < scores[i+1]:
    #             max_res += 1
    #             arr_max.append(scores[i+1])
    #         elif scores[i] > scores[i+1]:
    #             min_res += 1
    #             arr_min.append(scores[i+1])

    # if scores[0] < scores[1]:
    #     max_res -= 1
    
    
    # return arr_max, arr_min
    return len(arr_max), len(arr_min)

# print(breakingRecords([2,5,1,7]))
print(breakingRecords([12,24,10,24]))
print(breakingRecords([10,5,20,20,4,5,2,25,1]))
print(breakingRecords([3,4,21,36,10,28,35,5,24,42]))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     scores = list(map(int, input().rstrip().split()))

#     result = breakingRecords(scores)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
