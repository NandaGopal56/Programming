##Write a Python program to find the first repeating character in given string

def first_repeating_character(str):
    l=[]

    for i in str:
        if i in l:
            return i
        else:
            l.append(i)
    return None




print(first_repeating_character("abcdefd"))
print(first_repeating_character("abcabcdef"))
print(first_repeating_character("Good round"))