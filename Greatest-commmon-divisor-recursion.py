def GreatestCommonDivisor(a,b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only'
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1*b
    if b == 0:
        return a
    else:
        return GreatestCommonDivisor(b, a%b)

print(GreatestCommonDivisor(16, 48))

print(GreatestCommonDivisor(4, 48))

print(GreatestCommonDivisor(16, 16))

print(GreatestCommonDivisor(16, 32))