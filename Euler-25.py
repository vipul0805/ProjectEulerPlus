def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield len(str(a))
k=list(fib(23922))
t=int(input())
for i in range(t):
    n=int(input())
    for i in range(3*n,len(k)):
        if(k[i]==n):
            print(i+1)
            break
