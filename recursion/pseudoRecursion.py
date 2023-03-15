def russianDolls(dolls): 
    assert dolls >= 10, 'The values should be positive' #1) specify the constraints to pop up error so this is user interactive
    # also assert works if the condition breaks it will pop up an error if int(dolls) == dolls
    if dolls == 1: # 2) specify the base condition to terminate infinite loops
        return 'There is no dolls'
    else:
        return russianDolls(dolls-1) # 3) specify the recursive condition
print(russianDolls(8))