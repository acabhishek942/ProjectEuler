from time import time

t1 = time()

def isPalindrome(number):
  if str(number)[::-1] == str(number):
    return True
  return False
  
def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])
    

total = 0

for i in range(1000000):
  binaryRe = '{0:b}'.format(i)
  if isPalindrome(i) and isPalindrome(binaryRe):
    total += i
    
print (total)

print(time() - t1)
