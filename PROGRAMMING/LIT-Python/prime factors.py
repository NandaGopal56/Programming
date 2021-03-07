no=int(input("enter a number: "))
i=1
while i<=no:
    if no%i==0:
        #i is a factor
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c+=1
            j+=1
        if c==2:
            print(i)
    i=i+1



