def printPattern(n):
    
    if (n == 0 or n < 0):# base condition
        print(n) # this prints of only 0 or the value less than 0
        return
    
    print(n)
    printPattern(n-5) #it is called till the base condition is met 10, 5,

    print(n) # ascending N simply it prints original 10 as well as reduced 10 oops gotcha

printPattern(20)