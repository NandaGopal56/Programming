from sys import argv
class InvalidOptionError(Exception):
    pass
def main():
    option=srgv[1]
    if option=='-a':
        sum=0
        for arg in argv[2:]:
            sum=sum+int(arg)
        print(sum)
    elif option=='-m':
        mul=1
        for arg in argv[2:]:
            mul=mul*arg
        print(mul)
    else:
        raise InvalidOptionError
