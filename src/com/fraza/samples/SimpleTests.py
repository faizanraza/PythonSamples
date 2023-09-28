#!/anaconda3/bin/python

import datetime
import math
import os
import random
import re
import sys
    
def testBinary():
    bin_a = "{0:b}".format(10)
    print(bin_a)
    for c in list(bin_a):
        print(c)
        
    bin_list = list(bin_a)
    print(len(bin_list))
    print(len(bin_a))
    
    num = int('110',2)
    print(num)
    
    for i in range( len(bin_a) ):
        print(bin_a[i])

def andProduct(a, b):
    bin_a = "{0:b}".format(a)
    bin_b = "{0:b}".format(b)
    if( len(bin_b) > len(bin_a) ):
        return 0
    
    i = 0
    for i in range( len(bin_a) ):
        if bin_a[i] != bin_b[i]:
            break 
    
    print(i)
    
if __name__ == '__main__':
    #testBinary()
    #andProduct(13, 15)
    x = datetime.datetime.now()
    print(x)