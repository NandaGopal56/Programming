d=['zero','one','two','three','four','five','six','seven','eight','nine']

istr = "onezero two eight fourseven"

num=''
n=''
for i in istr:
    if i != " ":
        n=n+i
        if n in d:
            index = d.index(n.lower())
            num = num+str(index)
            n=''

print(int(num))
