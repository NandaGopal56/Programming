mat = [1, 5, 3, 2]
mat.sort()


print(mat)

for pointer in range(len(mat)-1, -1, -1):
    i = 0
    j = pointer-1
    while i<pointer-1:
        while j > 0:
            if mat[i]+mat[j] < mat[pointer]:
                i += 1
            elif mat[i]+mat[j] > mat[pointer]:
                j -= 1
            elif mat[i]+mat[j] == mat[pointer]:
                print(mat[i], mat[j], mat[pointer])
                break
        if i == j:
            break
        j -= 1
    i += 1

'''
https://www.geeksforgeeks.org/find-triplet-sum-two-equals-third-element/
'''

