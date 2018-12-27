from math import factorial
t=int(input())

for i in range(0,t):
    n,m=map(int,input().split())
    k=factorial(m+n)//(factorial(m)*factorial(n))
    print(k%(10**9+7))
