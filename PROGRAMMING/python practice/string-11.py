"""
Write a Python program to remove the characters which have odd index values of a given string
"""
def remove_odd_index_1(str):
    s=""
    for i in str:
        if str.index(i) % 2 != 0:
            str=str.replace(i,"@",1)
        elif str.index(i) % 2 ==0:
            s=s+i
            str=str.replace(i,"#",1)

    print(s)

def remove_odd_index_2(str):
    s=""
    for i in range(len(str)):
        if i%2==0:
            s=s+str[i]

    print(s)

remove_odd_index_1("abcdef")
remove_odd_index_1("pattanayak")
remove_odd_index_1("python")

remove_odd_index_2("abcdef")
remove_odd_index_2("pattanayak")
remove_odd_index_2("python")