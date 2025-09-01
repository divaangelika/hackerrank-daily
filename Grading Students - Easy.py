#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    grades_len = len(grades)
    for i in range(grades_len):
        if grades[i] < 38:
            continue
        else:
            grades_mod = grades[i] % 5
            mod_dif = 5 - grades_mod
            grades_dif = grades[i] + mod_dif

            if grades_dif - grades[i] < 3:
                grades[i] = grades_dif
            else:
                continue
    return grades

print(gradingStudents([73, 67, 38, 33]))

    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     grades_count = int(input().strip())

#     grades = []

#     for _ in range(grades_count):
#         grades_item = int(input().strip())
#         grades.append(grades_item)

#     result = gradingStudents(grades)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
