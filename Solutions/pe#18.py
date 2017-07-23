numberTriangle = [[0 for i in xrange(15)] for i in xrange(15)]

def enterToTriangle(numbers):
"""
Take the numbers in the form of string and enter it into the numberTriangle
"""
numberOfNumbers = numbers.split()
for i in range(len(numberOfNumbers)):
numberTriangle[len(numberOfNumbers)-1][i] = int(numberOfNumbers[i])

with open('number.txt') as numbersFile:
for line in numbersFile:
enterToTriangle(line)

for i in range(len(numberTriangle)-2, -1, -1):
for j in range(len(numberTriangle[i])):
if j==14:
break
numberTriangle[i][j] = numberTriangle[i][j] + max(numberTriangle[i+1][j], numberTriangle[i+1][j+1])
print numberTriangle