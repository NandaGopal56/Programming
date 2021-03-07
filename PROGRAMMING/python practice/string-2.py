str="nanda gopal pattanayak"
l=[]
d={}
for i in str:
    count=0
    if i.isalpha():
        if i not in l:
            for j in str:
                if i==j:
                    count+=1
            d[i]=count

print(d)