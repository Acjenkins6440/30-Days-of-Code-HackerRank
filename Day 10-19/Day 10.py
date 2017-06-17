#!/bin/python3

import sys


n = int(input().strip())
n = '{0:b}'.format(n)
q = 0
y = 0
for x in range(len(n)):
    if n[x] == '1':
        q += 1
        if q > y:
            y = q
    else: q = 0
print(y) 
