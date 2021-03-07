import re

str = "The rain in spain is sjhvsn"

#Check if the string has any a, r, or n characters:

x = re.findall("[a-zA-Z]{3}", str)

print(x)