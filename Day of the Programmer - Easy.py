#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # jan = 31
    feb = 28
    # mar = 31 
    # apr = 30
    # may = 31
    # jun = 30
    # jul = 31
    # aug = 31
    day_of_prog = 256

    months = [31,31,30,31,30,31,31]
    sum = 0

    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            feb = 29
    elif year == 1918:
        feb = 14
        # return f"26.09.1918"
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            feb = 29
    
    for i in months:
        sum += i
    
    sum += feb
    sum = abs(sum - day_of_prog)

    return f"{sum}.09.{year}"
    # print(feb)
    
    # return sum

print(dayOfProgrammer(2016)) #12
print(dayOfProgrammer(2017)) #13
print(dayOfProgrammer(1800)) #12
print(dayOfProgrammer(1984)) #12
print(dayOfProgrammer(1918)) #12



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     year = int(input().strip())

#     result = dayOfProgrammer(year)

#     fptr.write(result + '\n')

#     fptr.close()
