def decimalToBinary(value):
    assert value >= 0, 'The value should be postive'
    if value == 0:
        return 0
    else:
        return value % 2 + 10 * decimalToBinary(int(value / 2))
    # see here we take remainder value and multiply it with 10 so that we can grab the next value 1, 10, 101, 1010 
    # each subsequent times we will be adding 10
    # see according to binary rule we have to divide till we get zero so we are using it on floor

print(1%2)