"""
Write a Python program to remove the nth index character from a nonempty string
"""

def remove_nthindex(str,n):

    s=str[:n]
    p=str[n+1:len(str)]

    print(s+p)


remove_nthindex("nanda",3)
remove_nthindex("gopal",2)
remove_nthindex("python",0)
remove_nthindex("python",3)
remove_nthindex("python",5)