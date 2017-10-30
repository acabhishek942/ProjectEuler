"""
Execution time - 0.00025
"""

import time 
start = time.time()
def sumDigits(number):
    s = 0
    while n:
        s += number % 10
        number //= 10
    return s
upperBound = 100
result = 0

d = 1 
n = 2 

for i in range(2, upperBound + 1):
  temp = d
  if i % 3 == 0:
    c = 2 * (i // 3)
  else:
    c = 1
  d = n 
  n = c * d + temp
result = sumDigits(n)

print (result)
print (time.time() -  start)
