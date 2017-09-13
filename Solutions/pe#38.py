def is_pandigital(n, s=9):
    """
    returns true for pandigital numbers
    """
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)
    
    
largestPanDigital = 0
for i in range(9234, 9487):
    """
    see explanation in notes to understand
    search space optimization
    """
    number2 = i * 2
    
    if is_pandigital(int(str(i) + str(i * 2))):
        largestPanDigital = int(str(i) + str(i * 2))
print (largestPanDigital)
