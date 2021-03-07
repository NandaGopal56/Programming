def DecimalToBinary(n):
    assert int(n) == n , 'The parameter must be integer only'

    if n == 0:
        return 0
    else:
        return n%2 + 10 * DecimalToBinary(int(n/2))

print(DecimalToBinary(45))

print(DecimalToBinary(455))

print(DecimalToBinary(23))

print(DecimalToBinary(302))