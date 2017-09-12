from time import time

t1 = time()


def palindromeCreator(number, isOdd):
  if isOdd:
    return int(str(number)[:-1] + str(number)[::-1])
  return int(str(number) + str(number)[::-1])
  

def isPalindrome(number):
  if str(number)[::-1] == str(number):
    return True
  return False
    
total1 = 0

for j in range(2):
  isOdd = j % 2 == 0
  i = 1
  while palindromeCreator(i, isOdd) < 1000000:
    if isPalindrome('{0:b}'.format(palindromeCreator(i, isOdd))):
      total1 +=  palindromeCreator(i, isOdd)
    i += 1

print (total1)
print (time() - t1)
