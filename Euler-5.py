from functools import reduce
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    print (reduce(lambda x,y: x*y/gcd(x,y), range(1,n+1)))
