import math

amicableNumbers = []


def divisors(n):
"""
Get all the proper divisors of a number.
"""
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,int(n/i)])
    return list(set(divs))

for i in range(2, 10000):
    properDivisorsSum = sum(divisors(i))
    if properDivisorsSum > i:
        if sum(divisors(properDivisorsSum)) == i:
            amicableNumbers.extend([i, properDivisorsSum])

print (sum(amicableNumbers))​