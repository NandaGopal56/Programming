#Write a Python program to swap comma and dot in a string
#Sample string: "32.054,23"
#Expected Output: "32,054.23"

def swap_string(str):
    new_str=''

    for i in str:
        if i=='.':
            new_str=new_str+','
        elif i==',':
            new_str=new_str+'.'
        else:
            new_str=new_str+i
    print(new_str)


swap_string("32.054,23")