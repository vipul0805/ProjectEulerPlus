import math

t=int(input())
for i in range(t):
    n=int(input())
    power=pow(2,n)
    sum=0
    while(power!=0):
        k=power%10
        sum=sum+k
        power=power//10
    print(sum)
