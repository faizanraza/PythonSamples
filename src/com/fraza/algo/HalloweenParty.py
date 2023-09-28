#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/halloween-party/problem    

def halloweenParty(k):
    l = math.ceil(k/2)
    return int(l * (k-l))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        k = int(raw_input())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()
