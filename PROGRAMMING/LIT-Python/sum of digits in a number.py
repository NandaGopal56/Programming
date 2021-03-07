no=int(input("enter a number: "))
sum=0
while no!=0:
    last=no%10
    sum=sum+last
    no=no//10
print("sum is : ",sum)