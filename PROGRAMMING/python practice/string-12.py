"""
Write a Python program to count the occurrences of each word in a given sentence
"""

def word_count(str):
    str=str.split(" ")
    count={}
    for word in str:
        c=str.count(word)
        count[word]=c
    print(count)


word_count("the quick brown fox jumps over the lazy dog.")