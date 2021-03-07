str = "{}]()[]"
print("string is: ",str)

l = []
opening = ['{', '[', '(']
closing = ['}', ']', ')']

flag = True

for i in str:
    if i in opening or i in closing:
    
        if i in opening:
            l.append(i)

        elif i in closing:
            if len(l) >= 1:
                last = l[len(l)-1]
                if i == '}' and last =='{':
                    l.pop()
                elif i == ']' and last =='[':
                    l.pop()
                elif i == ')' and last =='(':
                    l.pop()
                else:
                    flag = False
                    print("UNBALANCED")
                    break
            else:
                l.append(i)
                flag = False
                print("UNBALANCED")
                break

if len(l) >= 1:
    flag = False
    print("UNBALANCED")


if flag:
    print("BALANCED")

print(l)
    
