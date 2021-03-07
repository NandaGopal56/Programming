def longest_subarray_with_sum_divisible_by_k(mat, k):
    final = []
    for i in range(len(mat)):
        subArray = []
        for j in range(i, len(mat)):
            subArray.append(mat[j])
            if sum(subArray) % k == 0:
                final.append(subArray)
                break
            
    return final



mat = [2, 7, 6, 1, 4, 5]
k = 3
print(longest_subarray_with_sum_divisible_by_k(mat, k))

'''
https://practice.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1
'''