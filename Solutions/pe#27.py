def primes_sieve(limit):
    """
    Generate all prime numbers less than or
    equal to the limit provided.
    """
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes
 
def equalMod(bList):
    """
    Given a list add all the negative values to the 
    original list.
    For Example : bList = [1, 2, 3] will return
                    [-1, -2, -3,  1, 2, 3]
    """
    bNegative = []
    for i in bList:
        bNegative.append(-i)
    return bList + bNegative
    
def is_prime(n):
    """
    Determine if the given number is prime or not.
    """
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
  
bPositives = primes_sieve(1000)
# as we determined why 'b' is always prime we pick only the
# prime numbers between (-1000, 1000) for 'b'
bList = equalMod(bPositives)

aMax = 0
bMax = 0
nMax = 0
"""
Iterate over all possible values of 'a' and
'b'(primes only) and count the n with the maximum count of primes
"""
for a in range(-999, 1001, 2):
    for b in bList:
        n = 0
        if b in [2, -2]:
            while is_prime(n*n + n*(a-1) + b):
                n += 1
        else:
            while is_prime(n*n + n*a + b):
                n += 1
                
        if n > nMax:
            nMax = n
            aMax = a
            bMax = b
        
print (aMax, bMax)
print (aMax * bMax)