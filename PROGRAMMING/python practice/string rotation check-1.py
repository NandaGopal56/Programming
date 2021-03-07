x='6 3'
x=x.split(' ')
size=int(x[1])

order='-11 -2 19 37 64 -18'
order=order.split()
#print(order)

final=[]

for i in range(len(order)):
    if i <= len(order)-size:
        l=[]
        l.append(order[i])
        l.append(order[i+1])
        l.append(order[i+2])

        #print(i, l)
        l.sort()


        count=0
        for j in l:
            if int(j) < 0:
                count+=1
                final.append(j)
                break
        if count==0:
            final.append(0)
#print(final)
for i in final:
    print(i,end=' ')