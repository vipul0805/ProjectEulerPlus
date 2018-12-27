import math

t=int(input())
for i in range(t):
    n=int(input())
    k=math.factorial(n)
    sum=0
    while(k!=0):
        num=k%10
        sum=sum+num
        k=k//10
    print(sum)
