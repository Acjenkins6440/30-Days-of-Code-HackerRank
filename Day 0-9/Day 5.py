#!/bin/python3

import sys


n = int(input().strip())
for i in range(1,11):
    y = n * i
    print("%d x %d = %d" % (n, i, y))
    
