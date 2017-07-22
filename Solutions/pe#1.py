def multiples_of_3():
    sum = 0
    for i in range(0, 1000, 3):
        sum = sum + i
    return (sum)
    
def multiples_of_5():
    sum = 0
    for i in range(0, 1000, 5):
        sum = sum + i
    return (sum)
    
def multiples_of_15():
    sum = 0
    for i in range(0, 1000, 15):
        sum = sum + i
    return (sum)
    
    
answer  =  multiples_of_3() + multiples_of_5() - multiples_of_15() 
print answer​