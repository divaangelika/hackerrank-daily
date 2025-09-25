#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here

    arr_len = len(bill)
    shared_items = 0
    b_actual = 0

    for i in range(arr_len):
        if i != k:
            shared_items += bill[i]

    # print(shared_items)
    b_actual = shared_items / 2
    # print(b_actual)
    res = b - b_actual
    # print("res=",res)

    if b_actual == b:
        print("Bon Appetit")
    else:
        print(int(res))

    # return res

bonAppetit([3, 10, 2, 9], 1, 12)      
# bonAppetit([3, 10, 2, 9], 1, 7)      

# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     bill = list(map(int, input().rstrip().split()))

#     b = int(input().strip())

#     bonAppetit(bill, k, b)
