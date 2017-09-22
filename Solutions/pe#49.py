import time
import itertools
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
  
def isPermutation(first, second):
  digits = [int(x) for x in str(first)]
  n_digits = len(digits)
  n_power = n_digits - 1
  permutations = itertools.permutations(digits)
  if second in [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]:
    return True
  return False


primeList =  sieveOfSundaram(9999)

primeListModified = [i for i in primeList if i > 1000]

print (len(primeListModified))

count = 0
for i in primeListModified:
  if i + 3330 in primeListModified and i + 6660 in primeListModified:
    if isPermutation(i + 3330, i) and isPermutation(i + 6660, i):
      print (str(i) + str(i + 3330) + str(i + 6660))
      count += 1
      if count == 2:
        break
print (time.time() - start)
