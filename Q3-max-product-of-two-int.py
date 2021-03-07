#How to find maximum product of two integers in the array where all integers are positive

Mylist = [1,2,20,3,44,55,65,78,23,12,25,99,1,2,34,23]

def findMaxProduct_1(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = f'{array[i]} * {array[j]}'
    print(f'{pairs} = {maxProduct}')

def findMaxProduct_2(array):
    max1 = max(array)
    array.remove(max1)
    max2 = max(array)
    print(f'{max1} * {max2} =  {max1*max2}')

findMaxProduct_1(Mylist)
findMaxProduct_2(Mylist)