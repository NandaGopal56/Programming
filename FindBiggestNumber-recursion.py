#finding time complexity

def findMaxNumRec(array, n):    #n is size of array ------------------------------M(n)
    if n == 1:                  #-------------------------------------------------O(1)
        return array[0]         #-------------------------------------------------O(1)
    else:
        return max(array[n-1], findMaxNumRec(array, n-1))   #---------------------M(n-1)

print(findMaxNumRec([1,2,3,44,54,33], 6))
print(findMaxNumRec([1,2,3,44,54,1,0,99,333], 9))

#M(n) = O(1) + M(n-1)