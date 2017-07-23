import math

def sum_digits(n):
    return sum([int(i) for i in str(n)])

nthFactorial = math.factorial(100)
print(sum_digits(nthFactorial))