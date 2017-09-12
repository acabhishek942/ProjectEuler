import math
import timeit

start_time = timeit.default_timer()
digitFactorials = {}

for i in range(10):
    digitFactorials[i] = math.factorial(i)
    
result = 0

for i in range(11, 2540161):
    sumofFacts = 0
    number = i
    while number>0:
        d = number % 10
        number = int(number / 10)
        sumofFacts += digitFactorials[d]
    if sumofFacts == i:
        result += i

print (result)
print (timeit.default_timer() - start_time)​
