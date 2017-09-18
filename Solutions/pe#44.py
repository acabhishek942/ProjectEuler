import math
import time

start = time.time()

def isPentagonal(number):
  pentagonal = (math.sqrt(24 * number + 1) + 1) / 6
  if pentagonal == int(pentagonal):
    return True
  return False
  
notFound =  True
i = 1

while notFound:
  i = i + 1
  n  = i * (3 * i -  1) / 2
  
  for j in range(i - 1, 0, -1):
    m = j * (3 * j -  1) / 2
    if isPentagonal(n + m) and isPentagonal(n - m):
      print (n -m)
      print (time.time() - start)
      break
      break
      break
