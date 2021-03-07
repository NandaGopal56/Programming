str = 'aaabbccdefffaghhh'

d = {}


for i in str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

for i in d:
    if d[i] == 1:
        print(i)
        break