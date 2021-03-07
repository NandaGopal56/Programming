#Write a Python program to count repeated characters in a string

def count_repeated_character(str):
    d={}
    for i in str:
        if str.count(i)>1:
            d[i]=str.count(i)
    l=[]
    for i in d:
        l.append(d[i])
    l=list(set(l))
    l.sort(reverse=True)

    for i in l:
        for j in d:
            if d[j] == i:
                print(j,i)

count_repeated_character("thequickbrownfoxjumpsoverthelazydog")