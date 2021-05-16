#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p = n = z = 0
    for e in arr:
        if e > 0:
            p += 1
        elif e < 0:
            n += 1
        else:
            z += 1
    print("{:0.6f}".format(p / len(arr)))
    print("{:0.6f}".format(n / len(arr)))
    print("{:0.6f}".format(z / len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
