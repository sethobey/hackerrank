#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(0, n):
        line = ""
        for j in range(0, n):
            line += "#" if n - j <= i + 1 else " "
        print(line)
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
