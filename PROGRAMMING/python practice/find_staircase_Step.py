def findStep( n) : 
    if (n == 1 or n == 0) : 
        return 1
    elif (n == 2) : 
        return 2
      
    else : 
        x = findStep(n - 2) 
        y =  findStep(n - 1)
        print('x and y :', x,y)
        return x+y

n = int(input())

if n > 20:
    print("Wrong Infrastructure")
else:
    print(findStep(n))