"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'
"""

str="restart"

s=str[0]

for i in str:
    if i==s:
        str=str.replace('r','$')

for i in str:
    if i=="$":
        str=str.replace(i,s,1)
        break

print(str)