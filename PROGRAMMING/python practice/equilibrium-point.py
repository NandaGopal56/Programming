def FindEquilibriumPoint(mat):
    totalSum = rightSum = sum(mat)
    leftSum = 0

    for i in range(len(mat)):
        rightSum = rightSum - mat[i]
        leftSum = totalSum - rightSum - mat[i]

        if leftSum == rightSum:
            return i
    return None
        
mat = [1,2,4,8,6,5,2,8,2,1,2,6]

print(mat[FindEquilibriumPoint(mat)])

'''
https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1
'''