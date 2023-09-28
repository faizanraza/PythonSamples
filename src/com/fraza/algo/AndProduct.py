#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/and-product/problem
# Complete the counterGame function below.
def andProduct(a, b):
    bin_a = "{0:b}".format(a)
    bin_b = "{0:b}".format(b)
    if( len(bin_b) > len(bin_a) ):
        return 0
    
    val = 0
    power = len(bin_a)-1
    for i in range( len(bin_a) ):
        if bin_a[i] != bin_b[i]:
            break
        if bin_a[i] == '1':
            val += 2**power
        power -= 1
    
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    for n_itr in xrange(n):
        ab = raw_input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

# test2
'''
8
112 127
80 95
32 47
176 191
32 47
32 47
192 207
176 191
'''
# result2
'''
112
80
32
176
32
32
192
176
'''