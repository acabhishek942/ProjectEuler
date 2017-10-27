"""
Use the continued fraction expression algo.
Approach and code referenced from mathblog anf dreamshire.
Execution time - 0.1445
"""

import time 
start = time.time()
import math
upperBound = 10000
result = 0

for n in range(2, upperBound + 1):
  r = limit =  int(math.sqrt(n))
  if limit ** 2 == n:
    continue
  period = 0
  d = 1
  m = 0
  a = limit
  
  while d !=1 or period == 0:
    d = (n - r * r) // d
    r = (limit + r) // d * d - r
    period += 1
  if period % 2 == 1: result += 1
      
print (result)
print (time.time() - start)
