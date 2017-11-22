import math
def chakravala(N):
  """
  Return (x, y) pair for the Diophantine equation 
  x^2 - N*y^2 = 1
  """
  p = p0 = int(round(math.sqrt(N)))
  a, b, k = p, 1, p*p - N
  if k == 0:
    # No solution exixts if N is perfect square.
    return
  while k != 1:
    # return if k in [-1, ±2, ±4] using the Bramhagupta lemma
    if k == -1 or abs(k) == 2 or (abs(k) == 4 and (a % 2== 0 or b % 2 == 0)):
      return ((a*a + N*b*b)//abs(k), 2*a*b//abs(k))
      
    # get value of 'm' such that k divides a + bm and absolute value of m^2 – N is minimum
    diff = (p + p0) % abs(k)
    pLeast = p0 - diff
    pMost = pLeast + abs(k)
    
    p = pLeast if (pLeast * pLeast - N) < (pMost * pMost - N) else pMost
    
    a, b, k = (p*a + N*b)//abs(k), (a + b*p)//abs(k), (p*p - N)//k
    
  return (a, b)
  
maxSolution = 0

for i in range(2, 1000):
  result = chakravala(i)
  if result is not None:
    if result[0] > maxSolution:
      maxSolution = result[0]
      maxX = i
    
print (maxX)
    
  
  ​
