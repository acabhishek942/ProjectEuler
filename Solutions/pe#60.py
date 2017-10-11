"""
Brute-force approach
Takes a significantly long time to run.
Not happy with the perfromance of this code.
Referernce from -  mathblog
"""

import random
import time
from collections import defaultdict
start =  time.time()


def is_prime(n):
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
  
def rabinMiller(n, k = 4):

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

def makePairs(primeList, index):
  primeHashMap = []
  for value in primeList[index:]:
    if is_prime(int(str(primeList[index]) + str(value))) and is_prime(int(str(value) + str(primeList[index]))):
      primeHashMap.append(value)
  return primeHashMap
    

primeList = sieveOfSundaram(30000)

primePairs = {}
primePairs = defaultdict(lambda:0, primePairs)
result =  2147483647 # max. int value in C#

for a in range(1, len(primeList)):
  if primeList[a] * 5 >  result:
    break
  if primePairs[a] == 0:
    primePairs[a] = makePairs(primeList, a)
  for b in range(a + 1, len(primeList)):
    if (primeList[a] + (primeList[b] * 4)) > result:
      break
    if not primeList[b] in primePairs[a]:
      continue
    if primePairs[b] == 0:
      primePairs[b] = makePairs(primeList, b)
    for c in range(b + 1, len(primeList)):
      if (primeList[a] + primeList[b] + (primeList[c] * 3) > result):
        break
      if not primeList[c] in primePairs[a] or not primeList[c] in primePairs[b]:
        continue
      if primePairs[c] == 0:
        primePairs[c] = makePairs(primeList, c)
      for d in range(c + 1, len(primeList)):
        if (primeList[a] + primeList[b] + primeList[c] + (primeList[d] * 2)) > result:
          break
        if not primeList[d] in primePairs[a] or not primeList[d] in primePairs[b] or not primeList[d] in primePairs[c]:
          continue
        if primePairs[d] == 0:
          primePairs[d] = makePairs(primeList, d)
        for e in range(d + 1, len(primeList)):
          if (primeList[a] + primeList[b] + primeList[c] + primeList[d] + primeList[e] >  result):
            break
          if not primeList[e] in primePairs[a] or not primeList[e] in primePairs[b] or not primeList[e] in primePairs[c] or not primeList[e] in primePairs[d]:
            continue
          if result > primeList[a] + primeList[b] + primeList[c] + primeList[d] + primeList[e]:
            result = primeList[a] + primeList[b] + primeList[c] + primeList[d] + primeList[e]
            print (result, primeList[a], primeList[b], primeList[c], primeList[d], primeList[e])
    

