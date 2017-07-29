def recurringCycleLength(number):
    """
    Given a number return the length of longest recurring cycle,
    of its unit fraction (ie 1/<number>)
    """
    recurringCycle = [1,]
    remainder = 1
    while (len(recurringCycle) < number):
        numerator = remainder * 10
        remainder = numerator % number
        if remainder == 0:
            return 0
        if remainder in recurringCycle:
            return len(recurringCycle)
        recurringCycle.append(remainder)
        
longestRecurringLength = 0

for i in range (1000, 1, -1):
    currentRecurringLength = recurringCycleLength(i)
    if currentRecurringLength == i - 1:
        # use the rule that maximum recurring cycle length of 1/d is d-1
        print (i, currentRecurringLength)
        break
    if currentRecurringLength > longestRecurringLength:
        longestRecurringLength = currentRecurringLength