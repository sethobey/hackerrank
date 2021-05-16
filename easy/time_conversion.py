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
    tod = s[-2:]
    h, m, s = s[:-2].split(":")
    if h == "12": h = "0"
    if tod == "PM":
        h = int(h) + 12
    return "{}:{}:{}".format(h, m, s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
