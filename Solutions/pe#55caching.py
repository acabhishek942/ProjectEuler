"""
With caching of non-lycherel numbers using dictionary.
Execution - 0.130s
"""

import time 

start = time.time()

isLycherel = {}
for i in range(10000):
  isLycherel[i] = True


def reverseNumber(number):
  # print (int(str(number)[::-1]))
  return int(str(number)[::-1])
  
def isPalindrome(number):
  return number == reverseNumber(number)
  
def isLycherel2(number):
  if not isLycherel[number]:
    return False
  allNumbers = [number]
  for i in range(50):
    if isPalindrome(number + reverseNumber(number)):
      for j in allNumbers:
        isLycherel[j] = False
      return False
    number = number + reverseNumber(number)
    allNumbers.append(number)
  return True
    
count = 0
for j in range(10, 10000):
  if isLycherel2(j):
    count += 1
    
print (count)
print (time.time() - start)
