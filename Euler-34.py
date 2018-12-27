from math import factorial
def summs(num):
    total=0
    while num>0:
        k=num%10
        total+=factorial(k)
        num=num//10
    return total

sum=0
N = int(input())
for j in range(10,N):
    tot = summs(j)
    if tot % j==0:
        sum += j
print(sum)
