import math

def divisors(n):
    """
    Get all the proper divisors of a number.
    """
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,int(n/i)])
    return list(set(divs))
    
abundantNumbers = []

"""
Find all abundant numbers
"""
for i in range (2, 28123):
    if sum(divisors(i)) > i:
        abundantNumbers.append(i)
        
sumOfAbundantNumbers = []

"""
Generate all numbers which can be written as sum of two abundant numbers.
"""
for i in range(len(abundantNumbers)):
    for j in range(i, len(abundantNumbers)):
        sumOfAbundantNumbers.append(i + j)
        
sumofNonAbundantNumbers = 0

for i in range(2, 28123):
    if i in sumOfAbundantNumbers:
        pass
    else:
        sumofNonAbundantNumbers += i

print (sumofNonAbundantNumbers)