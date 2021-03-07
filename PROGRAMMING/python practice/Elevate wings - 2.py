bets= [2, 202, 2, 3, 204, 4, 5, 1, 2, 3, 99, 2, 1,12]

final = []
temp =[]
i = 0

while i < len(bets)-1:

    temp.append(bets[i])
    for j in range(i+1, len(bets)):
        if bets[j] > bets[j-1]:
            temp.append(bets[j])
        else:
            
            break

    print(temp)
    temp = []
    i = j


print(final)
