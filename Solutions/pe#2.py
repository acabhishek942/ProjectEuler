fib3 = 2
fib6 = 0

result = 2
sum = 0

while (result < 4000000):
    sum += result
    result = 4*fib3 + fib6
    fib6 = fib3
    fib3 = result 
    
    
print(sum)