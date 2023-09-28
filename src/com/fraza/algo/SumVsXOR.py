#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/maximizing-xor/problem
# Complete the counterGame function below.
def sumXor(n):
    count = 0
    while( n > 1 ):
        count += 1 if n%2 == 0 else 0
        n /= 2
    return 2 ** count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
