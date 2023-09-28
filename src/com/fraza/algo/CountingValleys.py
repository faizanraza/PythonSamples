#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/counting-valleys/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
# Complete the countingValleys function below.
def countingValleys(n, s):
    n = 0
    d = 0
    for c in s:
        if d < 0:
            if c == 'D':
                d -= 1
            else:
                d += 1
                
            if( d == 0 ):
                n += 1
        else:
            if c == 'D':
                d -= 1
            else:
                d += 1   
    print (n)
    return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    