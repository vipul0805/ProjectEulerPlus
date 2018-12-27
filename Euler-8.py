#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    num=str(num)
    product=1
    product1=1
    for i in range(0,len(num)-k+1):
        product1=1
        for j in range(i,k+i):
            product1*=int(num[j])
        if(product1>product):
            product=product1
    if(product==1):
        print(0)
    else:
        print(product)
        
        
