"""
Own approach to this problem.
1. Iterate over odd composite numbers (N)
2. Iterate over all possible 'k' such that (N - 2k^2 > 0)
3. Check if the value (N - 2k^2) is prime or not.
4. Break all the loops when we find the number that doesn't satisfy (3)
5. Execution time  -  12.98s
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
  
primes = sieveOfSundaram(1000000)

for i in range(35, 1000000, 2):
  if i in primes:
    pass
  else:
     k =  1
     flag = False
     while i - 2 * k * k > 3:
       if i - 2 * k * k in primes:
         flag = True
         break
       k = k + 1
       
     if not flag:
       print (i)
       print (time.time() - start)
       break
