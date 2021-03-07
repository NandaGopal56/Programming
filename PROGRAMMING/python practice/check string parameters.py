if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum():
            print("True")
            break
    else:
        print("False")
    for i in s:
        if i.isalpha():
            print("True")
            break
    else:
        print("False")
    for i in s:
        if i.isdigit():
            print("True")
            break
    else:
        print("False")
    for i in s:
        if i.islower():
            print("True")
            break
    else:
        print("False")
    for i in s:
        if i.isupper():
            print("True")
            break
    else:
        print("False")


"""
In the first line, print True if S has any alphanumeric (a-z, A-Z and 0-9) characters. Otherwise, print False.
In the second line, print True if S has any alphabetical (a-z and A-Z) characters. Otherwise, print False.
In the third line, print True if S has any digits (0-9). Otherwise, print False.
In the fourth line, print True if S has any lowercase (a-z) characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase (A-Z) characters. Otherwise, print False.
"""