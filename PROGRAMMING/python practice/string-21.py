"""
Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters
"""

def check(str):
    count=0
    for i in range(4):
        if str[i].isupper():
            count+=1
    if count >= 2:
        str=str.upper()
    print(str)

check("NAnda")
check("gopal")
check("nAnDa Gopal")
check("nAnda Gopal")