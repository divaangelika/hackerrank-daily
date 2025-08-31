#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[0:2])
    minute_second = s[2:8]

    if hour == 12 and s[8:10] == 'AM':
        s = '00' + minute_second
    elif hour != 12 and s[8:10] == 'AM':
        new_hour = f"{hour:02}"
        s = new_hour + minute_second
    elif hour == 12 and s[8:10] == 'PM':
        new_hour = f"{hour:02}"
        s = new_hour + minute_second
    elif hour != 12 and s[8:10] == 'PM':
        hour += 12
        new_hour = f"{hour:02}"
        s = new_hour + minute_second

    
    return s 

print(timeConversion("02:01:00PM"))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()
