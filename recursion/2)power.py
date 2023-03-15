def pow(base, exp):
    assert int(exp) == exp, 'The value should be integer'
    if exp == 0:
        return 1
    else:
        return base * pow(base, exp-1)
    # see we have to multiply it by the times its give say 2^2 = 4 so already we have set 2 once so we have to run it for n-1 times so tht
    # we get perfect answer
print(pow(8,19))