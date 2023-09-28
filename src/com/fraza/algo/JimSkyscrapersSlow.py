 #!/bin/python

from __future__ import print_function

import os
import sys

#https://www.hackerrank.com/challenges/jim-and-the-skyscrapers/problem
# Complete the solve function below.
def solve(arr):
    paths = 0
    for i,h in enumerate(arr):
        j = i+1
        while (j < len(arr)):
            if(arr[j] > h):
                break
            else:
                if(arr[j] == h):
                    paths += 1
                j += 1       
    return paths*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()