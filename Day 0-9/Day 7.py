#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
k = []
for x in arr:
    k.insert(0,x)
k = (" ".join(str(i)for i in k))
print (k)
