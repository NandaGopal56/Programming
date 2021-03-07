#Write a Python program to find the first non-repeating character in given string

def first_non_repeating_character(str):
    d={}
    for c in str:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    for i in d:
        if d[i]==1:
            return i
    return None
    
    

print(first_non_repeating_character("abcdef"))
print(first_non_repeating_character("abcabcdef"))
print(first_non_repeating_character("aabbcc"))


"""
for i in str:
        if str.count(i)==1:
            return i
    return None

"""
"""
for i in str:
        counter=0
        for j in str:
            if i==j:
                counter+=1
        if counter==1:
            return i
"""