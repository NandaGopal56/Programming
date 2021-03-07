def logestPallindromeInAString(str):
    sub = ''
    final = []
    for i in range(len(str)):
        sub = sub+str[i]
        for j in range(i+1, len(str)):
            sub = sub+str[j]

            if sub == sub[::-1]:
                final.append(sub)
        sub = ''
    
    return final


print(logestPallindromeInAString("aaaabbaa"))

'''
https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0
'''