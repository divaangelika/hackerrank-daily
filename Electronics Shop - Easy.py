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

                if is_on_budget <= b and is_on_budget > max:
                    max = is_on_budget
                else:
                    continue

    if max == 0:
        return -1
    
    return max

# Test cases
keyboards = [
    12, 25, 37, 41, 19, 22, 35, 50, 60, 75,
    10, 15, 20, 30, 40, 45, 55, 65, 70, 80,
    5, 7, 9, 11, 13, 16, 18, 21, 23, 26,
    28, 29, 31, 32, 33, 34, 36, 38, 39, 42,
    43, 44, 46, 47, 48, 49, 51, 52, 53, 54,
    56, 57, 58, 59, 61, 62, 63, 64, 66, 67,
    68, 69, 71, 72, 73, 74, 76, 77, 78, 79,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

drives = [
    3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
    2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
    32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
    42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
    62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
    72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
    82, 83, 84, 85, 86, 87, 88, 89, 90, 91,
    92, 93, 94, 95, 96, 97, 98, 99, 100
]

budget = 150

print(getMoneySpent(keyboards, drives, budget))

# print(getMoneySpent([3, 1], [5, 2, 8], 10))   # Expected: 9
# print(getMoneySpent([4], [6], 5))             # Expected: -1
# print(getMoneySpent([40, 50, 60], [5, 8, 12], 60))  # Expected: 58
# print(getMoneySpent([10, 12], [5, 3], 15))    # Expected: 15
# print(getMoneySpent([1, 2, 3], [2, 3, 4], 9)) # Expected: 7
# print(getMoneySpent([21, 22, 23], [30, 40], 20)) # Expected: -1

# print(getMoneySpent([3,1],[5,2,8],10))
# print(getMoneySpent([4],[5],5))
# print(getMoneySpent([40,50,60],[5,8,12],60))
# print(getMoneySpent([183477,732159,779867],[598794,596985,156054],374625))

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
