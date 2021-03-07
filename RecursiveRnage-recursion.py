def RecursiveRnage(n):
    if n == 1:
        return 1
    else:
        return n + RecursiveRnage(n-1)

print(RecursiveRnage(6))
print(RecursiveRnage(4))
print(RecursiveRnage(5))