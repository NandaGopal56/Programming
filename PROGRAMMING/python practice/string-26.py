#Write a Python program to print the index of the character in a string



def print_position(str):
    for i in range(len(str)):
        print("current pos of {} is {}".format(str[i],i))


print_position("w3resource")