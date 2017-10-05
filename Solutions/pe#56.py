"""
Execution time -  0.269
"""

import time 
start =  time.time()
maxDigitSum = 0

def getDigitSum(number):
  digitSum = 0
  while number > 0:
    digitSum += number % 10
    number //=  10
  return digitSum
  
# for i in range(99, 1, -1):
#   for j in range(99, 1, -1):
#     testNumber = i ** j
#     digitalSum = getDigitSum(i ** j)
#     if digitalSum > maxDigitSum:
#       maxDigitSum = digitalSum

for i in range(100):
  for j in range(100):
    if getDigitSum(i ** j) >  maxDigitSum:
      maxDigitSum = getDigitSum(i ** j)

print (maxDigitSum)
print (time.time() - start)
