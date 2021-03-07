#What is the time Complexity of the below code ?

# Printing Unordered Pairs

def PrintUnOrderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(str(array[i])+","+str(array[j]))

PrintUnOrderedPairs([1,2,3,4,5,6])