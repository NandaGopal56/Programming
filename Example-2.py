#print Pairs

#Whst is the runtime of the below code ?

def PrintPairs(array):
    for i in array:         #-----------------O(n^2)  }
        for j in array:     #-----------------O(n)    }     O(n^2)+O(n) = O(n^2)
            print(str(i)+","+str(j))    #--------O(1)

PrintPairs([1,2,3,5,4])

#Final time complexity is O(n^2)