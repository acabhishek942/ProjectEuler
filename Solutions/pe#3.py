import math
def isprime(n):
    """Returns True if n is prime."""
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

def getNextPrime(previousPrime):
    """
    Given a prime number, return the next prime.
    """

    while True:
        previousPrime = previousPrime + 1
        if isprime(previousPrime):
            return previousPrime
        
        
def largestPrimeFactor(number):
    startingPrime = 2
    half = math.sqrt(number)
    while startingPrime < half:
        if number % startingPrime == 0:
            number = number / startingPrime
            if number == 1.0:
                return startingPrime
        startingPrime = getNextPrime(startingPrime)

#print (math.sqrt(600851475143))

print (largestPrimeFactor(600851475143))