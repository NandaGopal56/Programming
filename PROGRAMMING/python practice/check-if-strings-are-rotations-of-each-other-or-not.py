def checkRotation(s1, s2):
    final = s1
    for i in s1:
        final = final.replace(i, '', 1)
        final = final+i
        if final == s2:
            return True
    return False
    
s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"
c1 = "mightandmagic"
c2 = "andmagicmigth"
print(checkRotation(s1, s2))
print(checkRotation(c1, c2))


'''
https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1
'''