def longest_sub_array_with_sum(mat, maxSum):
    final = []
    for i in range(len(mat)):
        subArray = []
        for j in range(i, len(mat)):
            subArray.append(mat[j])
            if sum(subArray) == maxSum:
                final.append(subArray)
                break
            
    return final



mat = [10, 5, 2, 7, 1, 9]
maxSum = 15
print(longest_sub_array_with_sum(mat, maxSum))

'''
https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

'''