"""
Use the property of the modulo operator.

(a+b) % c = ((a % c) + (b % c) )% c

Execution time - 0.414
"""

import time

start =  time.time()
result = 0
modulo = 10000000000
longMaxValue = 9223372036854775807

for i in range(1, 1001):
  temp = i
  for j in range(1, i):
    temp *= i
    if temp >= longMaxValue / 1000:
      temp %= modulo
  result += temp
  result %= modulo
  
  
print (result)
print (time.time() - start)
