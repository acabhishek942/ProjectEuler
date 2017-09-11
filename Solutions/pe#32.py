def is_pandigital(n, s=9):
    """
    this function only works for 1-9 pandigital
    """
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)

pandigitalSet = set()


for i in range(2,  60):
    if i < 10:
        start = 1234
    else:
        start =123 
    for j in range(start, 10000//i): # to make sure the product doesn't exceed to more than 4 digits
        if is_pandigital(str(i) + str(j) + str(i*j)):
            pandigitalSet.add(i*j)

print ("Sum of products =" +  str(sum(pandigitalSet)))
