#check rotation in two given string

s1='ABCDE'
s2='CDEAB'

count=0
diff=abs(s1.index(s1[0])-s2.index(s1[0]))
#print(diff)

for i in range(len(s1)):
    if i+diff <= len(s1)-1:
        if s1[i] == s2[i+diff]:
            count+=1
            #print(count)
    else:
        if s1[i] == s2[i+diff-len(s1)]:
            count+=1
            #print(count)

if count==len(s1):
    print('True')
else:
    print('False')