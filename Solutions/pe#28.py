def sumDiagonal(number):
    """
    Give the sum of diagonal elements of a 
    nxn square of numbers
    """
    if number == 1:
        return 1
    return (4*number*number - 6*(number - 1) + sumDiagonal(number - 2))
    
print (sumDiagonal(1001))