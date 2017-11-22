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

def leftTruncatable(prime):
  count = 0
  while prime > 0:
    if not prime/10 in primes:
      count += 1
  if count > 0:
    return False
  return True


def rightTruncatable(prime):
  count = 0
  prime = int(str(prime)[::-1])
  while prime > 0:
    if not prime/10 in primes:
      count += 1
  if count > 0:
    return False
  return True


primes = sieveOfSundaram(1000000)

primeSum = 0

count = 0

while count < 12:
  for i in primes:
    if leftTruncatable(i) and rightTruncatable(i):
      primeSum += i
      count += 1

print (count)

