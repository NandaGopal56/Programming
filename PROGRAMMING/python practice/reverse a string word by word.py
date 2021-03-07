s="nanda is best"
s=s.split(" ")
print(s)
for i in range(len(s)):
    j=s[i]
    s[i]=j[::-1]

x=" ".join(s)
print(x)
