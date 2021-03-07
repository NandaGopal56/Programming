#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s=s.split(' ')
    l=[]
    str=''
    for i in s:
        for j in range(len(i)):
            if j==0:
                str=str+i[0].capitalize()
            else:
                str=str+i[j]
        l.append(str)
        str=''
    s=' '.join(l)
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
