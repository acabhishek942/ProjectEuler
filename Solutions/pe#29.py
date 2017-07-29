distinctValues = []
for a in range(2, 101):
    for b in range(2, 101):
        if a**b not in distinctValues:
            distinctValues.append(a**b)
            
print (len(distinctValues))