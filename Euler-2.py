#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    b = 2
    a = 0
    result =2
    summed = 0
    while (result <n):
        summed += result
 
        result = 4*b +a
        a = b
        b = result
    print(summed)

