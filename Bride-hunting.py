mat = [[0, 0, 1, 1, 0, 1, 1, 1, 1],
       [0, 0, 0, 1, 0, 1, 0, 0, 1]]

data = {}

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 1:
            calc = 0
            if i != 0 and j != 0:
                if mat[i][j-1] == 1:
                    calc += 1
                if mat[i][j+1] == 1:
                    calc += 1
                if mat[i-1][j] == 1:
                    calc += 1
                if mat[i-1][j-1] == 1:
                    calc += 1
                if mat[i-1][j+1] == 1:
                    calc += 1
                if mat[i+1][j] == 1:
                    calc += 1
                if mat[i+1][j-1] == 1:
                    calc += 1
                if mat[i+1][j+1] == 1:
                    calc += 1
            print(calc)
            break