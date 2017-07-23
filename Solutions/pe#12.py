from collections import defaultdict

def primes(n):
    """
    Returns a dictionary with prime factors as the key.
    and the power of prime factor as its value.
    
    For Example : primes(28) will return 
    {2 : 2, 7 : 1}
    """
    primfac = {}
    primfac = defaultdict(lambda: 0, primfac)
    while (n % 2) == 0:
        primfac[2] += 1 
        n //= 2
    d = 3
    while d*d <= n:
        while (n % d) == 0:
            primfac[d] += 1  # supposing you want multiple factors repeated
            n //= d
        d += 2
    if n > 1:
       primfac[n] = 1
    return primfac
    
def triangleNumber(n):
    """
    Returns the nth trianle number.
    """
    return sum(range(n+1))

nthTriangle = 1
noDivisors = 1
while noDivisors < 500:
    currentTriangle = triangleNumber(nthTriangle)
    primeDict  = primes(currentTriangle)
    noDivisors = 1
    for i in primeDict:
        noDivisors = noDivisors * (primeDict[i] + 1)
    nthTriangle += 1
    
print (currentTriangle)