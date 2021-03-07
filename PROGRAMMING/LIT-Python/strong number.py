no=int(input("enter a number: "))
record=no
sum=0
while no>0:
    last=no%10
    fact=1
    while last>0:
        fact=fact*last
        last-=1
    sum=sum+fact
    no=no//10

print(sum)
if sum==record:
    print("strong number")
else:
    print("not a strong number")