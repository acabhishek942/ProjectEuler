import math
def isprime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
    
def generatePrimes(upperLimit):
    primeList = []
    for i in range(upperLimit):
        if isprime(i):
            primeList.append(i)
    return primeList

result = 1

for i in generatePrimes(20):
    a = math.floor(math.log(20,2)/math.log(i,2))
    result = result * (i**a)
print (result)