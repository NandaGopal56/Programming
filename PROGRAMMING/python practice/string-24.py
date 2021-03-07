def reverse_string_words(str):
    str=str.replace(".",' ')
    str=str.split(" ")

    str.reverse()
    str=" ".join(str)
    str=str+'.'
    return str


print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))
