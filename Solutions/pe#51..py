"""
Execution time - 0.155
"""

import time

start = time.time()

def getFiveDigitPattern():
  return [[1,0,0,0,1],
          [0,1,0,0,1],
          [0,0,1,0,1],
          [0,0,0,1,1],]
          

def getSixDigitPattern():
  return [[1, 1, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 1],
          [1, 0, 0, 1, 0, 1],
          [1, 0, 0, 0, 1, 1],
          [0, 1, 1, 0, 0, 1],
          [0, 1, 0, 1, 0, 1],
          [0, 1, 0, 0, 1, 1],
          [0, 0, 1, 1, 0, 1],
          [0, 0, 1, 0, 1, 1],
          [0, 0, 0, 1, 1, 1]]
 
 
 
def fillPattern(pattern, number):
  fillPattern =  [0] * len(pattern)
  temp =  number
  for index, i in enumerate(pattern):
    if i == 1:
      fillPattern[index] = temp % 10
      temp = int(temp / 10)
    else:
      fillPattern[index] = -1
  return fillPattern
  
def generateNumber(repNumber, filledPattern):
  temp = 0
  #print (filledPattern)
  for i in filledPattern:
    temp =  temp * 10
    if i == -1:
      temp += repNumber
    else:
      temp += i
  return temp


def getfamilySize(repNumber, pattern):
  familySize = 1
  for i in range(repNumber + 1, 10):
    if isPrime2(generateNumber(i, pattern)):
      familySize += 1
  return familySize
  
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True
    
fiveDigitPattern = getFiveDigitPattern()
sixDigitPattern = getSixDigitPattern()
result = 326766

for i in range(11, 1000, 3):
  if i % 5 == 0:
    continue
  patterns = sixDigitPattern
  
  
  for j in range(len(patterns)):
    for k in range(3):
      if patterns[j][0] == 0 and k == 0:
        continue
      pattern = fillPattern(patterns[j], i)
      candidate = generateNumber(k, pattern)
      
      if candidate < result and isPrime2(candidate):
        if getfamilySize(k, pattern) == 8:
          result = candidate
          
print (result)
print (time.time() - start)        
      
