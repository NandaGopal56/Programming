str=input("enter a string: ")

print(str.count("a")+str.count("A"))
str=str.replace("a","ngp").replace("A","NGP")
print(str.count("a")+str.count("A"))

str=str.replace(","," ")

str=str.replace("!"," ")

str=str.replace(":"," ")

str=str.replace("."," ")
print(str.split(" "))