#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/maximizing-xor/problem
# Complete the counterGame function below.
def maximizingXor(l, r):
    max = 0
    j = r
    while( j > l ):
        i = j-1
        while( i >= l ):
            x = i ^ j
            if( x > max ):
                max = x
            i -= 1
            j -= 1
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(raw_input())

    r = int(raw_input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
