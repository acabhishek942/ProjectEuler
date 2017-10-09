import random
"""
1. generate corner numbers using the algo described.
2. Check if the generated number is prime or not (expensive step),
   using Rabin-Miller algorithm
3. Run the loop against the condition given in the question

Execution time - 0.771
"""
def rabinMiller(n, k = 10):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    

noOfPrimes = 3
s1 = 2
currentNumber = 9

while noOfPrimes / ((2 * s1) + 1) > 0.10:
  s1 += 2
  for i in range(4): # this loop should run 3 times
    currentNumber += s1
    if rabinMiller(currentNumber):
      noOfPrimes += 1
      
print (s1 + 1)  
