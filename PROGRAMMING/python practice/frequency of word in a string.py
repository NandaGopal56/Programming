str=input("enter a string: ").strip()

list=str.split()

list2=[]

for i  in list:
    if i not in list2:
        list2.append(i)


for i in list2:
    c=list.count(i)
    print(i,c)