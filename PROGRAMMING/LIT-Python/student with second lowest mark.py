if __name__ == '__main__':
    d={}
    list1=[]
    list2=[]
    list3=[]
    for _ in range(int(input())):
        name = input()
        x = float(input())
        d.update({name:x})
for i in d:
    list1.append(d[i])
x=len(list1)

for i in range(x):
    for j in range(i+1,x):
        #list1[i], list1[j]= list1[i], list1[j]
        if list1[j] < list1[i]:
            list1[j], list1[i]= list1[i], list1[j]

print(list1)

y=min(list1)
z=list1.count(y)
for i in range(z):
    list1.remove(y)

print(list1)

list2.append(min(list1))

for i in d:
    if d.get(i) in list2:
        list3.append(i)

list3.sort()
for data in list3:
    print(data)

"""
i/p-
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
o/p-
Berry
Harry

to print the name of students with second lowest number in alphabetical order 

"""