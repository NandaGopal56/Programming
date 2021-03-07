#Finding time complexity

def FindBiggestNumber(array):
    biggestNumber = array[0] #-------------------------------O(1)
    for index in range(1, len(array)): #-------------------------------O(n)
        if array[index] > biggestNumber: #-------------------------------O(1)
            biggestNumber = array[index] #-------------------------------O(1)
    return biggestNumber    #-------------------------------O(1)


print(FindBiggestNumber([1,2,3,5,4,7,89,4]))

print(FindBiggestNumber([1,20,322,55,4,7,89,4]))

print(FindBiggestNumber([1,299,322,51,4,7,896,4]))

