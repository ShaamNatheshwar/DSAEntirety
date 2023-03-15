def printNum(n, m, Flag):
    # n - input variable or the number which we wanna pattern
    # m - shows the current as well as a helper variable
    # flag - tells us whether we can add or not

    print(m) # not n as its a constant value

    if Flag == False and n == m: # specifying base condition we dont wanna print after input value
        return
    
    if Flag:
        if m-5 > 0: # if the value is more than zero we will continue to print pattern
            return printNum(n,m-5, True)
        else: # if the value exceeds we will jst print the exceeded value and continue to add values until the condition n == m is met..once done we will print
            return printNum(n, m-5, False)
    else: # use of recursion we are only printing m so the value is added to stack then checks for the condition once done we get the value
        return printNum(n, m+5, False)

n = 33
printNum(n,n , True)