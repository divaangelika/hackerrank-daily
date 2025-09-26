#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar_len = len(ar)
    # count = 0
    res = 0
    total_even = 0
    total_odd = 0
    total = 0
    arr_distinct = []

    for i in range(ar_len):
        found = False
        for k in range(len(arr_distinct)):
            if ar[i] == arr_distinct[k]:
                found = True
                break
        
        if found == False:
            arr_distinct.append(ar[i])

    # [1,2,1,2,1,3,2]
    # [10,20,20,10,10,30,50,10,20]
    for j in range(len(arr_distinct)):
        count = 0
        for p in range(ar_len):
            if arr_distinct[j] == ar[p]:
                count += 1

        # return count        
        # res = count % 2
        # return res
        # break
        # print("count=",count)
        print(arr_distinct[j],"muncul",count,"kali")

        if count == 1:
            total += 0
            print("total=",total)
            # total_even += 0
            # total_odd += 0
        else:
            total += count // 2
            print("total",total)
        # elif count % 2 == 0:
        #     total_even += count // 2 #0 #0
        #     print("total even=",total_even)
        # elif count % 2 == 1:
        #     total_odd += count % 2 #3=1 #3=1
        #     print("total odd=",total_odd)
        # else:
        #     total_even, total_odd = 0
            

    # res = total_even + total_odd 
    res += total

    return res, arr_distinct, ar
    
        
        # total += res


    # return arr_distinct
    # return count
    # return res
    return res




print(sockMerchant(7,[1,2,1,2,1,3,2])) #2
print(sockMerchant(9,[10,20,20,10,10,30,50,10,20])) #3
print(sockMerchant(10,[1,1,3,1,2,1,3,3,3,3])) #4



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
