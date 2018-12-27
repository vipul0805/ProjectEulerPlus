#!/bin/python3

import sys
l=[]

for i in range(100,999,1):
    for j in range(i,999,1):
        k=i*j
        if(str(k)==str(k)[::-1] and k not in l):
            l.append(k)
l.sort()
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(len(l)):
        if(l[i]>=n):
            break
    print(l[i-1])
    
