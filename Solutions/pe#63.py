"""
Executuion time - 0.0001
Mathblog approach
"""

import time
import math
start = time.time()

lower  = 0 
result = 0
n = 1 
while lower < 10:
  lower = int(math.ceil(10 ** ((n-1.0)/n)))
  result += 10 - lower
  n+=1
  
print (result)
print (time.time() - start)
