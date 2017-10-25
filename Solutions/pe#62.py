"""
Execution - 0.021
"""

import time
start = time.time()

myDict = {}

n = 345

while True:
  cube = n ** 3
  digits = ''.join(sorted(str(cube)))
  if digits in myDict:
    myDict[digits] += [cube]
  else:
    myDict[digits] = [cube]
  if len(myDict[digits]) == 5:
    print min(myDict[digits])
    break
  n += 1
print (time.time() - start)
