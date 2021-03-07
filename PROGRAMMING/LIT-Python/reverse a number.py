no=int(input("enter a number: "))
rev=0
while no!=0:
    last=no%10
    rev=rev*10+last
    no=no//10

print("reverse is : ",rev)