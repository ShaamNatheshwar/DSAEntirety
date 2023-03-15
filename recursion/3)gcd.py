def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The value should be positive'
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
    #according to the eucledian rule say 48,   18 remainder is 12 so 18, 12 remainder is 6 so 12,6 == 0 hence the gcd is gotta be 6
    # b % remainder ==0 == gcd so b is interchanged with a and function is called recursively till we reach 0 more like the russian doll some
print(gcd(98,29))