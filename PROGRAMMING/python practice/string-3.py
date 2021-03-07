"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""



def string_change(str):

    s=""

    if len(str)<2:
        print('invalid string')
    else:
        for i in range(2):
            s=s+str[i]
        for j in range(2,0,-1):
            s=s+str[-j]

    print(s)

string_change("w3resource")
string_change("w3")
string_change("Nanda Gopal")