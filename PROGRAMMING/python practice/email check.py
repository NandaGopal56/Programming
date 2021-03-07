import email.utils
import re
#n=input()
str1="vineet <vineet.iitg@gmail.com>"
str2="vineet <vineet.iitg@gmail.com>"

temp1=email.utils.parseaddr(str1)
temp2=email.utils.parseaddr(str2)

temp1 = list(temp1)
temp2 = list(temp2)

temp1 = str(temp1[1])
temp2 = str(temp2[1])

if temp1[0]!="." or temp1[7]!=".":
    temp1 = temp1.replace("@", " ").replace(".", " ")
temp1 = temp1.split(" ")
print(temp1)

while("" in temp1) :
   temp1.remove("")

if temp2[0]!=".":
    temp2 = temp2.replace("@", " ").replace(".", " ")
temp2 = temp2.split(" ")

while("" in temp2) :
    temp2.remove("")

f1=str(temp1[0])
f2=str(temp2[0])

regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
check=re.compile('[@!#$%^&*()-_.<>?/\|}{~:]')

if len(temp1)==3:
    if len(temp1[2]) <= 3 and temp1[2].isalpha() and regex.search(temp1[2]) == None:
         if temp1[1].isalpha():
            if  regex.search(temp1[0]) == None and check.search(f1[0])==None :
                print(str1)
if len(temp2)==3:

    if len(temp2[2]) <= 3 and temp2[2].isalpha() and regex.search(temp2[2]) == None:
        if temp2[1].isalpha():
            if regex.search(temp2[0]) == None and check.search(f1[0])==None:
                print(str2)











