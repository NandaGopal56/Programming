str="nanda gopal pattanayak"
l=[]
new=[]
for i in str:
    if i!=' ':
        if i not in l:
            count=str.count(i)
            l.append(i)
            x=i*count
            new.append(x)
print(new)