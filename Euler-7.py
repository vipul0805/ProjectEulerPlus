m=1000000
a=[]
prime = [True for i in range(m+1)]
p = 2
while (p * p <= m):
         
    if (prime[p] == True):
            for i in range(p * 2, m+1, p):
                prime[i] = False
    p += 1
     
for p in range(2, m):
    if prime[p]:
        a.append(p)
print(len(a))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    for i in range(0,len(a)):
        if(i==n-1):
            print(int(a[i]))
        
