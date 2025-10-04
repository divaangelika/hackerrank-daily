#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards_len = len(keyboards)
    drives_len = len(drives)
    is_on_budget = 0
    max = 0

    for i in range(keyboards_len):
        for j in range(drives_len):
            # is_on_budget = keyboards[i] + drives[j]
            
            if keyboards[i] < b and drives[j] < b:
                is_on_budget = keyboards[i] + drives[j]

                if is_on_budget <= b:
                    max = is_on_budget
                else:
                    continue

    if max == 0:
        return -1
    
    return max

print(getMoneySpent([3,1],[5,2,8],10))
print(getMoneySpent([4],[5],5))
print(getMoneySpent([40,50,60],[5,8,12],60))
print(getMoneySpent([183477,732159,779867],[598794,596985,156054],374625))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     bnm = input().split()

#     b = int(bnm[0])

#     n = int(bnm[1])

#     m = int(bnm[2])

#     keyboards = list(map(int, input().rstrip().split()))

#     drives = list(map(int, input().rstrip().split()))

#     #
#     # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
#     #

#     moneySpent = getMoneySpent(keyboards, drives, b)

#     fptr.write(str(moneySpent) + '\n')

#     fptr.close()
