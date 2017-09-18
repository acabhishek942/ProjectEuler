import time
start_time = time.time()


pandigitalSet =  set()
def is_pandigital(n, s=9):
    """
    this function only works for 1-9 pandigital
    """
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)

for i in range(2,  60):
    if i < 10:
        start = 1234
    else:
        start =123 
    for j in range(start, 10000//i): # to make sure the product doesn't exceed to more than 4 digits
        if is_pandigital(str(i) + str(j) + str(i*j)):
            pandigitalSet.add(i*j)
            


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
    
    
primes =  sieveOfSundaram(7654321)

largestPrime =  2
for i in primes:
  if is_pandigital(i, len(str(i))):
    largestPrime = i
    
print (largestPrime)
print("--- %s seconds ---" % (time.time() - start_time))
