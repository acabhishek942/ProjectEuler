def getDigits(number):
    """
    Get the digit^5 of the given number in a list.
    """
    digitList = []
    while number:
        digit = number % 10
        digitList.append(digit)
        number //= 10
    return digitList
    
def verifyDigitPowerSum(number):
    """
    Verify that number is equal to sum of
    its digits to the 5th power 
    """
    sumof5thPower = 0
    digits = getDigits(number)
    for i in digits:
        sumof5thPower += i**5
    if sumof5thPower == number:
        return True
    return False

toPower5 = {}

for i in range(10):
    toPower5[i] = i ** 5
total = 0
for i in range(100, 295245):
    if max(getDigits(i))**5 < i:
        if verifyDigitPowerSum(i):
            total += i
            
print (total)