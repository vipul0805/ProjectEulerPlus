n=int(input())
sum2=0
for i in range(100,600000):
    sum1=0
    k=str(i)
    for j in range(0,len(k)):
        sum1+=int(k[j])**n
    
    if sum1==i:
        sum2+=sum1
print(sum2)
