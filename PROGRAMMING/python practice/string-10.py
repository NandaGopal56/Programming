"""
Write a Python program to change a given string to a new string where the first and last chars have been exchanged
"""

def string_change(str):
    first=str[0]
    second=str[len(str)-1]

    #print(str[1:len(str)-1])

    str=second+str[1:len(str)-1]+first

    print(str)



string_change("nanda")
string_change("gopal")
string_change("truck")