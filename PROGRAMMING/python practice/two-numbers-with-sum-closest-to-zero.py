def sumClosestToZero(l):
    final = []
    sums = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            x = l[i]+l[j]
            final.append((l[i],l[j],x))
            sums.append(int(x))

    sums.sort(reverse=True)
    for tuples in final:
        if tuples[2] == sums[0]:
            return tuples
    



l = [-21, -67, -37, -18, 4, -65]
m = [-8, -66, -60]
print(sumClosestToZero(l))
print(sumClosestToZero(m))

'''
https://practice.geeksforgeeks.org/problems/two-numbers-with-sum-closest-to-zero1737/1
'''