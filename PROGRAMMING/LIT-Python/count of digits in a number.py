no=int(input("enter a no: "))
count=0
while no!=0:
    no=no//10
    count+=1

print("no of digits in the number is ",count)