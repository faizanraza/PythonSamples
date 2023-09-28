#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/and-product/problem
# Complete the counterGame function below.
def andProduct(a, b):
    ldiff = math.log(b,2) - math.log(a,2)
    if( ldiff >= 1 ):
        return 0
    
    bin_a = "{0:b}".format(a)
    bin_list = list(bin_a)
    count_bin = len(bin_list) - 1
    
    val = 0
    for c in bin_list:
        if c == "0":
            break
        val += 2**count_bin
        count_bin -= 1
    
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