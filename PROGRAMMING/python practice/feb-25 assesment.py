def check_prime(n):
    counter=0
    if n<=1:
        return 0
    else:
        for i in range(1,n+1):
            if n%i==0:
                counter+=1
        if counter == 2:
            return 1
        else:
            return -1

def composite_prime_list(l):
    prime = []
    compsite = []
    all = []
    for digit in l:
        if check_prime(digit)==0:
            compsite.append(digit)
        elif check_prime(digit)==1:
            prime.append(digit)
    all.append(prime)
    all.append(compsite)
    return all

if __name__ == '__main__':
    l=[1,2,3,4,5,6,7,89,9,7,5,6,3,2,45,6,6,8,9,5,4,5,8,9,5,2]
    print(l)
    print(composite_prime_list(l))

