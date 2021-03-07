n = 9
na = ['A','B','C','D','E','F','G','H','I']
matches = 14
scores = [('A','B',0,1),('A','C',1,5),('A','B',3,5),('B','C',4,5),('C','B',3,5),('D','E',5,4),('D','E',3,5),
          ('I','H',1,0),('F','G',4,2),('H','G',4,4),('F','H',1,4),('F','G',4,3),('H','G',2,2),('F','H',1,2)]



team_scores = {}
for team in na:
    team_scores[team] = 0

gf = {}
ga = {}
gd = {}
for team in na:
    gf[team] = 0
    ga[team] = 0
    gd[team] = 0

for match in scores:
    if match[2] > match[3]:
        team_scores[match[0]] += 2
        team_scores[match[1]] += 0

    elif match[2] < match[3]:
        team_scores[match[1]] += 2
        team_scores[match[0]] += 0

    elif match[2] == match[3]:
        team_scores[match[0]] += 1
        team_scores[match[1]] += 1

print('team scores:',team_scores)

for match in scores:
    gf[match[0]] += match[2]
    ga[match[0]] += match[3] 

    gf[match[1]] += match[3]
    ga[match[1]] += match[2]

print('goal for:',gf)
print('goal against:',ga)

for team in gf:
    gd[team] += gf[team] - ga[team]

print('goal difference:',gd)

scores = []
for score in team_scores:
    scores.append(team_scores[score])

print('unsorted scores:',scores)
scores.sort(reverse=True)
print('sorted scores:',scores)

duplicate = []

for score in scores:
    if scores.count(score) > 1:
        duplicate.append(score)

duplicate = list(dict.fromkeys(duplicate))
scores = list(dict.fromkeys(scores))

print('duplicate scores:',duplicate)

winner_rank_wise = []

for score in scores:
    if score not in duplicate:
        for team in team_scores:
            if team_scores[team] == score:
                winner_rank_wise.append(team)
    else:
        print("----------------------------------------------------------------------------------------------------------------")
        duplicate_teams = []
        for team in team_scores:
            if team_scores[team] == score:
                duplicate_teams.append(team)
        print('duplicate teams:',duplicate_teams)

        duplicate_gf = []
        duplicate_gd = []
        for team in duplicate_teams:
            duplicate_gf.append(gf[team])
            duplicate_gd.append(gd[team])
        print("duplicate_gf:",duplicate_gf)
        print("duplicate_gd:",duplicate_gd)

        sorted_duplicate_gd = duplicate_gd.copy()
        sorted_duplicate_gd.sort(reverse=True)
        print("sorted_duplicate_gd",sorted_duplicate_gd)

        sorted_duplicate_team_by_gd = []
        for i in sorted_duplicate_gd:
            for j in duplicate_gd:
                if i == j:
                    index = duplicate_gd.index(j)
                    duplicate_gd.remove(j)
                    duplicate_gd.insert(index,'#')
                    sorted_duplicate_team_by_gd.append(duplicate_teams[index])
        print("sorted_duplicate_team_by_gd:", sorted_duplicate_team_by_gd)

        temp = []
        temp_gf = []
        duplicate_score = 0
        while duplicate_score <= len(sorted_duplicate_gd)-1:
            if sorted_duplicate_gd.count(sorted_duplicate_gd[duplicate_score]) == 1:
                winner_rank_wise.append(sorted_duplicate_team_by_gd[duplicate_score])
                duplicate_score += 1
            else:
                try:
                    while duplicate_score <= duplicate_score + sorted_duplicate_gd.count(sorted_duplicate_gd[duplicate_score]) - 2:
                        temp.append(sorted_duplicate_team_by_gd[duplicate_score])
                        temp_gf.append(gf[sorted_duplicate_team_by_gd[duplicate_score]])

                        duplicate_score += 1
                except:
                    print("exception raised")

                print("temp:",temp)
                print("temp_gf:",temp_gf)

                sorted_temp = []
                sorted_temp_gf = temp_gf.copy()
                sorted_temp_gf.sort(reverse=True)

                for i in sorted_temp_gf:
                    index = temp_gf.index(i)
                    temp_gf.remove(i)
                    temp_gf.insert(index,'#')
                    sorted_temp.append(temp[index])
                print("sorted_temp:",sorted_temp)
                print("sorted_temp_gf:",sorted_temp_gf)

                for i in range(len(sorted_temp_gf)):
                    if sorted_temp_gf.count(sorted_temp_gf[i]) == 1:
                        winner_rank_wise.append(sorted_temp[i])
                    else:
                        winner_rank_wise.append(sorted_temp[i].lower())

print("----------------------------------------------------------------------------------------------------------------")

winner_rank_wise  = list(dict.fromkeys(winner_rank_wise))

print('team','score','goal-diff','goal-for','goal-against')

for winner in winner_rank_wise:
    print(winner,'  ',team_scores[winner.upper()],'      ',gd[winner.upper()],'        ',gf[winner.upper()],'       ',ga[winner.upper()])


'''
................................................MY TRIED TEST CASES.........................................

n = 9
na = ['A','B','C','D','E','F','G','H','I']
matches = 14
scores = [('A','B',7,5),('A','C',7,5),('A','B',6,5),('B','C',2,5),('C','B',4,5),('D','E',5,4),('D','E',3,5),
          ('I','H',1,0),('F','G',4,2),('H','G',3,4),('F','H',1,4),('F','G',2,3),('H','G',2,1),('F','H',4,2)]

##################################################################################################################################

n = 9
na = ['A','B','C','D','E','F','G','H','I']
matches = 14
scores = [('A','B',2,5),('A','C',3,5),('A','B',6,5),('B','C',2,5),('C','B',4,5),('D','E',5,4),('D','E',3,5),
          ('I','H',1,0),('F','G',4,2),('H','G',3,4),('F','H',1,4),('F','G',2,3),('H','G',2,1),('F','H',4,2)]

##################################################################################################################################

n = 5
na = ['SPAIN','ITALY','ENGLAND','FRANCE','GERMANY']
matches = 3
scores = [('ITALY','SPAIN',3,0),('SPAIN','FRANCE',1,1),('ITALY','FRANCE',0,2)]

##################################################################################################################################

n = 9
na = ['A','B','C','D','E','F','G','H','I']
matches = 14
scores = [('A','B',0,0),('A','C',0,0),('A','B',0,0),('B','C',0,0),('C','B',0,0),('D','E',0,0),('D','E',0,0),
          ('I','H',0,0),('F','G',0,0),('H','G',0,0),('F','H',0,0),('F','G',0,0),('H','G',0,0),('F','H',0,0)]

##################################################################################################################################

n = 9
na = ['A','B','C','D','E','F','G','H','I']
matches = 14
scores = [('A','B',1,2),('A','C',1,3),('A','B',2,2),('B','C',0,2),('C','B',0,1),('D','E',1,0),('D','E',0,0),
          ('I','H',0,0),('F','G',0,9),('H','G',2,1),('F','H',0,0),('F','G',0,0),('H','G',0,0),('F','H',0,0)]

'''