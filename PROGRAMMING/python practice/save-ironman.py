def saveIronman(str):
    s = ''
    for i in str:
        if i.isalpha():
            s = s+i
    s = s.lower()
    if s == s[::-1]:
        return True



str1= "I am :IronnorI Ma, i"
str2 = "Ab?/Ba"

print(saveIronman(str1))
print(saveIronman(str2))

'''
https://practice.geeksforgeeks.org/problems/save-ironman0227/1
'''