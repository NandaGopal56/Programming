bets = [10,15, 20, 5, 19, 21, 22, 10, 25, 26, 27, 15, 30, 40, 10, 50]

check = 0
score = []
temp = []
for i in range(len(bets)):
    if bets[i] > check:
        temp.append(bets[i])

        for j in range(i+1, len(bets)):
            if bets[j] > bets[i]:
                temp.append(bets[j])
                check = bets[j]
            else:
                break
    score.append(sum(temp))
    temp = []

print(score, sum(score))