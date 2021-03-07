for i in range(1,7):
    if i%2 != 0:
        for j in range(4):
            print(i,end='')
        print(i+1)

    else:
        print(i+1,end='')
        for k in range(4):
            print(i,end='')
        print()