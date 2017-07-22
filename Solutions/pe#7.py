upperLimit = 10001
counter = 1
primes = [2, ]


while len(primes) < upperLimit:
    counter += 2
    j = 0
    isPrime = True
    while primes[j]**2 < counter:
        if counter % primes[j] == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(counter)
        
print (primes[-1])