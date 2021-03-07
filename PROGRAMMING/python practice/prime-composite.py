def check_prime(num):
    count = 0
    for j in range(1,num+1):
        if num % j == 0:
            count +=1
    if count == 2:
        return 1
    return 0


def prime_composite_list(inp):
    prime = []
    composite = []

    for i in inp:
        if check_prime(i) == 1:
            prime.append(i)
        elif check_prime(i) == 0:
            composite.append(i)
    prime.sort(reverse=True)
    composite.sort(reverse=True)
    x = []
    x.append(prime)
    x.append(composite)
    return x


if __name__ == '__main__':
    inp = []
    count = int(input('enter the count:'))
    for _ in range(count):
        inp.append(int(input()))
    print(check_prime(inp[1]))

    result = prime_composite_list(inp)
    print(result)