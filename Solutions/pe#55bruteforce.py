"""
Execution - 0.258s
"""

import time 

start = time.time()

def reverseNumber(number):
  # print (int(str(number)[::-1]))
  return int(str(number)[::-1])
  
def isPalindrome(number):
  return number == reverseNumber(number)
  
def isLycherel2(number):
  for i in range(50):
    if isPalindrome(number + reverseNumber(number)):
      return False
    number = number + reverseNumber(number)
  return True
    
count = 0
for j in range(10, 10000):
  if isLycherel2(j):
    count += 1
    
print (count)
print (time.time() - start)
