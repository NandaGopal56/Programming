def findSubArrayWithZeroSum(mat):
    final = []
    for i in range(len(mat)):
        subArray = []
        for j in range(i, len(mat)):
            subArray.append(mat[j])
            if sum(subArray) == 0:
                final.append(subArray)
    return final



mat = [4, 2, -3, 4, -2, -2, 1, 6, -6]
print(findSubArrayWithZeroSum(mat))

'''
https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

'''