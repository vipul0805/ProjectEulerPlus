numm = 600851475143
newnumm = numm
largestFact = 0
 
int counter = 2
while (counter * counter <= newnumm):
    if (newnumm % counter == 0):
        newnumm = newnumm // counter
        largestFact = counter
    else 
        counter+=1
if (newnumm > largestFact):
    largestFact = newnumm
