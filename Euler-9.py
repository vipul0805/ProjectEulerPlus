import cmath

def getFib(n):
    #Given which fibonacci number we want, calculate its value
    lsa = (1 / cmath.sqrt(5)) * pow(((1 + cmath.sqrt(5)) / 2), n)
    rsa = (1 / cmath.sqrt(5)) * pow(((1 - cmath.sqrt(5)) / 2), n)
    fib = lsa-rsa
    #coerce to real so we can round the complex result
    fn = round(fib.real) 
    return fn 

#Demo using the function
s = ''
for m in range(0,3000):
    s = s + '(' + str(getFib(m))

print(s)
