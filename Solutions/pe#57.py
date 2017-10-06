"""
used pattern for generating num and den

num(k + 1) = num(k) + 2 * den(k)
den(k + 1) = num(k + 1) - den(k)

Execution time - 0.005
"""

import time
start = time.time()
numerator = 3
denominator = 2

result = 0
for i in range(1000):
  numerator = numerator + 2 * denominator
  denominator = numerator - denominator
  if len(str(numerator)) > len(str(denominator)):
    result += 1
    
print (result)
print (time.time() - start)
