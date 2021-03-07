"""
Write a Python function that takes a list of words and returns the length of the longest one
"""

def string_length(l):

    c=0
    for i in l:
        if len(i) > c:
            c=len(i)
    return c

print (string_length(['nanda','go','gopal','pattanayak']))

print (string_length(['write','awesome','bad','good']))