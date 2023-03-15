def sumOfDigits(value):
    assert value >= 0 and int(value) == value,'The value is negative'
    if value == 0:
        return 0
    else:
        return int((value % 10) + sumOfDigits(value // 10))
    # see we have to find the digits which can be done using adding reminder and divisor so we are using modulo and floor division
    # see whatever value it may be if do modulo of 10 u will get a reminder of 0-9 but when u do floor division we will have values more than 10
    # so we have to call floor division of 10 recursively

print(sumOfDigits(110))