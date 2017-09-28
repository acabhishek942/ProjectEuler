"""
Brute-force solution with modified search space.
Execution time - 3.22
"""

import time 
startTime = time.time()


def isPerm(first , second):
  temp = first
  permDict = {}
  for i in range(10):
    permDict[i] = 0
  while temp > 0:
    permDict[temp % 10] += 1
    temp = int(temp / 10)
  temp = second
  while temp > 0:
    permDict[temp % 10] -= 1
    temp = int(temp / 10)
    
  for i in permDict.values():
    if i !=0:
      return False
  return True


start = 1
found = False
result = 0

while not found:
  start *= 10
  for i in range(start, int(start*1.6)):
    found = True
    for j in range(2, 7):
      if not isPerm(i, i *j):
        found = False
        
    if found:
      result = i
      break
    
print (result)
print (time.time() - startTime)
  
