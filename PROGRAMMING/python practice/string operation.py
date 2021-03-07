
text='''
Pester 3.0 has been released! To see a list of changes in this version, refer to the What's New in Pester 3.0?'''

text=text.strip().split(' ')
temp=text
print(text)

length=len(text)
print(length)
for i in range(length):
    text[i]=text[i][::-1]

print(text)
try:
    for i in range(0,length,2):
        j=i+1
        text[i],text[j]=text[j],text[i]
except:
    print('exception is raised: one extra element that canot be sorted according to the given format')
print(text)
text=temp

list1=[]
final=[]
for i in range(0,length,2):
    l=[]
    l.append(text[i])
    l.append(text[i+1])
    list1.append(l)
print(list1)

for i in range(0,len(list1),2):
    j=i+1
    try:
        list1[i],list1[j]=list1[j],list1[i]
    except:
        print('exceptions raised: extra elemrnt that canot be sorted according to the given format ')
print(list1)


for i in list1:
    final.extend(i)
print(final)



s='1'
print(s)

s=s.zfill(4)
print(s)

