 #!/bin/python

from __future__ import print_function

import os
import sys

#https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem
# Complete the solve function below.
def solve(arr):
    paths = 0
    keyval = {
        }
    for i,h in enumerate(arr):
        for h1 in keyval.keys():
            if h1 < h:
                keyval.pop(h1)
            elif h1 == h:
                paths += keyval[h1]

        if (h in keyval):
            keyval[h] += 1
        else:
            keyval[h] = 1
      
    return paths*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()