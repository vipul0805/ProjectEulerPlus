def count(name):
    sum=0
    for i in name:
        sum=sum+(ord(i)-64)
    return sum


n=int(input())
l=[]
for i in range(0,n):
    name=input()
    l.append(name)
l.sort()
q=int(input())
for i in range(0,q):
    name=input()
    k=count(name)
    final=k*(l.index(name)+1)
    print(final)
    
