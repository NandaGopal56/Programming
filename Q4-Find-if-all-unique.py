# Determine if a list has all unique characters using python list

myList = [1, 20, 22, 34, 45, 67, 2, 45, 22, 45, 65, 45]

def isUnique(array):
    a = []
    for i in array:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)

print(isUnique(myList))