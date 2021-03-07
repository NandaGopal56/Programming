N=input().split(" ")
A=input().split(" ")
M=input().split(" ")
B=input().split(" ")


x=list(map(int,A))
y=list(map(int,B))

x=set(x)
y=set(y)

z=x.symmetric_difference(y)
z=list(z)
for i in range(len(z)):
    for j in range(i+1,len(z)):
        if z[i]>z[j]:
            z[i],z[j]=z[j],z[i]
#print(z)
for data in z:
    print(data,end="\n")

