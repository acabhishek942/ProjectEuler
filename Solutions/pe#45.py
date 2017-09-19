import math
import time

start =  time.time()

def isPentagonalAndTriangular(number):
  pentagonal = (math.sqrt(24 * number + 1) + 1) / 6
  triangular = (math.sqrt(8 * number + 1) - 1) / 2
  if pentagonal == int(pentagonal) and triangular == int(triangular):
    return True
  return False
  
i = 143
notFound =  True

while notFound:
  i = i + 1
  hexagonal = i * (2*i - 1)
  if isPentagonalAndTriangular(hexagonal):
    print (hexagonal)
    notFound = False
print (time.time() -  start)
