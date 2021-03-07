
#checking how many  chacters of a string doesnot change position when string is altered

str="alphxxdida"

rev=str[::-1]
print(rev)
counter=0
for i in range(len(str)):
    if str[i] == rev[i]:
        counter+=1

print(counter)