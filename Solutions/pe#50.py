"""
1. Generate a prime list.
2 Generate a cumulative primeSum list
3. Run an outer loop in forward direction (i)
4. Run an inner loop in backwards direction from index 'i' to 0
5. if primeSum[i] -  primeSum[j] in PrimeList
6. we update the result as primeSum[i] -  primeSum[j], else we continue doing steps 3 to 5

Execution time  -  4.32s
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
  
  return primes[:1] + primes[2:]

def cumulativePrimeSum(primeList):
  cumulativeSum = [0]
  primeSum = 0
  for i in primeList:
    primeSum += i
    cumulativeSum.append(primeSum)
    
  return cumulativeSum
  
primeList = sieveOfSundaram(1000000)
cumulativePrimeSum = cumulativePrimeSum(primeList)
numberOfPrimes = 0



for i, value in enumerate(cumulativePrimeSum):
  for j in range(i-(numberOfPrimes + 1), -1, -1):
    if cumulativePrimeSum[i] -  cumulativePrimeSum[j] > 1000000:
      break
    if cumulativePrimeSum[i] -  cumulativePrimeSum[j] in primeList:
      numberOfPrimes =  i - j
      result = cumulativePrimeSum[i] -  cumulativePrimeSum[j]
print (result, numberOfPrimes)
print (time.time() -  start)​
