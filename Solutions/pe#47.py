"""
Technique is brute-force.
1. A function to return the number of prime factors of a number.
2. Start iteration from (2*3*5*7) and continue.
3. Execution time - 1.802 
"""


import time
start =  time.time() 
  
def numberOfPrimeFactors(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return len(set(factors))

result = 2 * 3 * 5 * 7
consec = 1

while consec < 4:
  result += 1
  if numberOfPrimeFactors(result) == 4:
    consec += 1
  else:
    consec = 0
    
print (result - 3)
print (time.time() - start)

