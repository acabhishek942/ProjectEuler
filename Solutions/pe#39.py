import math
from fractions import gcd

import time
start_time = time.time()

def numberofSolutins(perimeter):
    count = 0  
    mLimit = int(math.sqrt(perimeter/2))
    for m in range(2, mLimit):
        if (perimeter/2) % m == 0:
            if m%2 == 0:
                k = m+1
            else:
                k=m+2
            while k < 2* m and k<=perimeter/2*m:
                if (perimeter/2*m) % k == 0 and gcd(k, m) == 1:
                    d = perimeter / 2 / (k * m)
                    n = k - m
                    a = d*(m * m - n * n)
                    b = 2 * d * n * m
                    c = d * (m * m + n * n)
                    count = count + 1
                k = k + 2
    return count
count = 0
maximizedSolution =  0

# print (numberofSolutins(1000))


for i in range(2, 1000):
    number =  numberofSolutins(i)
    if number > count:
        count = number
        maximizedSolution =  i
print (count, maximizedSolution)
print("--- %s seconds ---" % (time.time() - start_time))
