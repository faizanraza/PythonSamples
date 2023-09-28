#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/counter-game/problem
# Complete the counterGame function below.
def counterGame(n):
    Louise = False
    while( n>1 ):
        Louise = not Louise
        x = math.log(n,2)
        if ( x == int(x) ):
            n = n / 2
        else:
            n = n - 2 ** int(x)
    if (Louise):
        return "Louise"
    else:
        return "Richard"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
