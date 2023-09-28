#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/flipping-bits/problem
# Complete the flippingBits function below.
def flippingBits(n):
    flip_n = ~n
    flip_n += 2**32
    return flip_n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()