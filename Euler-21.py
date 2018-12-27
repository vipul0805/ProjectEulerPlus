import math  
def sum_factors(n):  
    result = []
    for i in range(1, int(n**0.5) + 1):
         if n % i == 0:
            result.extend([i, n//i])
    return sum(set(result)-set([n]))

def amicable_pair(number):
    result = 0
    for x in range(1,number+1):
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            result  += x
    return result

t=int(input())
for i in range (0,t):
    final=0
    N=int(input())
    
    print(amicable_pair(N))
