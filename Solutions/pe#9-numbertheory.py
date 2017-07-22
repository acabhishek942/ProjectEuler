import math
from fractions import gcd
found = False
s = 1000
mLimit = int(math.sqrt(s/2))
for m in range(2, mLimit):
    if (s/2) % m == 0:
        if m%2 == 0:
            k = m+1
        else:
            k=m+2
        while k < 2* m and k<=s/2*m:
            if (s/2*m) % k == 0 and gcd(k, m) == 1:
                d = s / 2 / (k * m)
                n = k - m
                a = d*(m * m - n * n)
                b = 2 * d * n * m
                c = d * (m * m + n * n)
                print (a,b,c)
                found = True
                break
            k = k + 2