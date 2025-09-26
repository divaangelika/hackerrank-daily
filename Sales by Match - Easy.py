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
    count = 0
    container = []
    # flag = 0

    for i in range(ar_len):
        # count = 0
        # container.append(ar[i])
        for k in range(ar_len-1):
            if ar[i] == ar[k+1]:
                # container.append(ar[i])
                container.append(ar[k+1])

                # if i == 0 and k == 0:
                #     container.append(ar[i])

                # count += 1
                # print("iterasi:",k)
                # print(ar[i],ar[k+1])
                # print("count",count)
            # if k > 0:
            #     break
        # container.append(ar[i])
        # if i == 1:
        #     container.append(ar[i])
        #     break

    
    # return count
    return container

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
