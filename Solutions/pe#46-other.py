"""
Subtract the prime from the primelist and check if the 
remainder is twice of a squared.

Execution time - 0.136s
"""


import math
import time 

start =  time.time()
def isTwiceSquare(number):
  squareTest = math.sqrt(number / 2)
  return squareTest == int(squareTest)
  
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
  
primeList = sieveOfSundaram(10000)

result = 1
notFound = True
 
while notFound:
    result += 2
 
    j = 0
    notFound = False
    while result >= primeList[j]:
        if isTwiceSquare(result-primeList[j]):
            notFound = True
            break;
        j =  j + 1
    if not notFound:
      print (result)
      break
    
print (time.time() - start)
