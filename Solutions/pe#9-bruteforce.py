circumfurence = 1000
found = False
for a in range (1, int(circumfurence/3)):
    for b in range(a, int(circumfurence/2)):
        c = circumfurence - a - b
        if c*c == a*a + b*b:
            found = True
            print (a*b*c)
            break