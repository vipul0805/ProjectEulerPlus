#All test cases are not cleared
from time import time
t=time()

a=[0]*100
c=0
for i in range(2,100):
    if a[i]==0:
        for j in range(i*i,100,i):
            continue
        a[c]=i
        c=c+1
print(a)

n=1
ctr=0
while(ctr<=1000):
    ctr=1
    triang=n*(n+1)/2
    x=triang
    i=0
    n=n+1
    while(a[i]<=x):
        b=1
        while(x%a[i]==0):
            b=b+1
            x=x//a[i];
        i=i+1
        ctr=ctr*b
print(triang)
print("took time",time()-t)
