t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    n1=n//3
    if(n%5>=1):
        n1=n//3-1
    print(n1)    
    n1=3*n1*(n1+1)//2

    n2=n//5
    if(n%5==0):
        n2=n//5-1   
    print(n2)
    n2=5*n2*(n2+1)//2

    n3=n//15
    print(n3)
    n3=15*n3*(n3+1)//2
    print(n1,n2,n3)
    print(n1+n2-n3)
    
t = int(input().strip())
for a0 in range(t):
    n = int(input())
    a=(n-1)%3;
    a=n-1-a
    a=a//3
    print(a)
    b=(n-1)%5
    b=n-1-b
    b=b//5
    print(b)
    d=(n-1)%15
    d=n-1-d
    d=d//15
    print(d)
    c= 3*a*(a+1)//2 + 5*b*(b+1)//2 - 15*d*(d+1)//2
    print(3*a*(a+1)//2,5*b*(b+1)//2,15*d*(d+1)//2)
    print(c) #print the answer
    
