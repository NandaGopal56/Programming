d=['zero','one','two','three','four','five','six','seven','eight','nine']

istr = "input  enter a string : )one two seven nine two having one seven of four"
istr = istr.lower()

dic = {}
real = {}
num = ""

l=[]

for i in d:
    if i in istr:
        for _ in range(istr.count(i)):
            #print(i,istr.index(i))
            dic[istr.index(i)] = i 
            real[istr.index(i)] =  d.index(i)   
            index = istr.index(i)
            istr =  istr.replace(i , "$"*len(i) , 1)
            l.append(index)
l.sort()
#print(istr)
#print(l)
#print(dic)
#print(real)

for i in l:
    num = num + str(real[i])

print(num)