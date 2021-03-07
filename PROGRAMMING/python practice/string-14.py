"""
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). Go to the editor
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white
"""



str="red, white, black, red, green, black"

str=str.split(",")

l=[]
for word in str:
    if word.strip() not in l:
        l.append(word.strip())

l.sort()
print(l)