str="nanda gopal pattanayak,very good.this is a very awesome,food.however;its not like -others"

str=str.replace(',',' ').replace('.',' ').replace(';',' ').replace('-',' ')
str=str.split(' ')
l=[]
for word in str:
    if word != '':
        l.append(word)

for word in l:
    print(word)