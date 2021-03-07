no = int(input('enter a no:'))
r = int(input("enter the kth factor you want to see:"))

count = 0

for i in range(1,no+1):
    if no%i == 0:
        #print("factor:",i)
        count += 1  
        if count == r:
            
            print("kth factor is :",i)
            break
else:
    print("kth factor not found")
