str = "python is a is very is a good programming is a programming very language"

str = str.split(' ')
l = []
size = []
for word in str:
    size.append(len(word))

size.sort()
size = set(size)

for i in size:
    temp=[]
    for word in str:
        if i == len(word):
            temp.append(word)
    temp.sort()
    l.extend(temp)

str = ' '.join(l)

print(str)