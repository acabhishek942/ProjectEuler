"""
Brute-Force with factorial caching.

Execution time - 0.004
"""

import math
import time

start = time.time()

factorialList = []

for i in range(101):
  factorialList.append(math.factorial(i))

result = 0  
for n in range(101):
  for r in range(n):
    if factorialList[n] / (factorialList[r] * factorialList[n - r]) > 1000000:
      result += 1
      
print (result)
print (time.time() - start)
