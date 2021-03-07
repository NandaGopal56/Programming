#Find the missing number from a list of integers from 1 to 100

#HINT - 1+2+3...+n = n(n+1)/2

Mylist = list(range(1,101))
Mylist.remove(73)


def FindMissingNumber(Mylist, n):
    sum1 = (n*(n+1))/2
    sum2 = sum(Mylist)
    print(f"missing number is : {sum1-sum2}")

FindMissingNumber(Mylist, len(Mylist)+1)
