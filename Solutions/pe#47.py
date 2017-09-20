"""
Technique is brute-force.
1. A function to return the number of prime factors of a number.
2. Start iteration from (2*3*5*7) and continue.
3. Execution time - 2.654 
"""


import time
start =  time.time()
def sieveOfSundaram(number):
  """
  SOS ia an algorithm to calculate all the primes below
  a given value.
  """
  nNew = int((number -2) / 2)
  
  marked = [0] * number
  primes = []
  
  
  for i in range (1, nNew):
      j = i
      while i + j + (2*i*j) <= nNew:
          marked[i + j + (2*i*j)] = 1
          j += 1
  if number > 2:
    primes.append(2)
          
  for i, value in enumerate(marked):
    if i < nNew:
      if not value:
          primes.append(2*i + 1)
  
  return primes
  
  
def numberOfPrimeFactors(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return len(set(factors))
  
primeList = sieveOfSundaram(100000)
result = 2 * 3 * 5 * 7
consec = 1

while consec < 4:
  result += 1
  if numberOfPrimeFactors(result) >= 4:
    consec += 1
  else:
    consec = 0
    
print (result - 3)
print (time.time() - start)

