def sumOfSquares(number):
    """
    Return the sum of squares of all natural numbers till the argument provided.
    """
    return number**3/3 + number**2/2 + number/6
    
def sumOfNumber(number):
    """
    Return the sum of all natural numbers till the given number
    """
    return (number**2 + number)/2
    
print (int(sumOfNumber(100)**2 - sumOfSquares(100)))