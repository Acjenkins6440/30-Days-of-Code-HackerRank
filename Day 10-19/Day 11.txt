#!/bin/python3

import sys


arr = []
p = -63
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
s = len(arr)
for i in range(0,(s-2)):
    for x in range(0,(s-2)):
        q = arr[i][x] + arr[i][x+1] + arr[i][x+2] + arr[i+1][x+1] + arr[i+2][x] + arr[i+2][x+1] + arr[i+2][x+2]
        p = max(q,p)
print (p)
