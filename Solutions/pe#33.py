from fractions import gcd

denProduct = 1
nomProduct = 1

for i in range(1,10):
    for denominator in range(1, i):
        for numerator in range(1, denominator):
            if denominator * (10*numerator + i) == (10*i + denominator) * numerator:
                denProduct = denProduct * denominator
                nomProduct = nomProduct * numerator

denProduct /= gcd(nomProduct, denProduct)
print (denProduct)
