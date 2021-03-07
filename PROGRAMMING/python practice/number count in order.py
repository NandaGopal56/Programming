
#First, the character 1  occurs only once. It is replaced by (1,1) .
#Then the character 2 occurs three times, and it is replaced by (3,2) and so on.


if __name__=="__main__":
    no ='1222311'
    l=[]
    temp=''
    count=0
    for digit in no:
        count += 1
        if digit != temp:
            counter = 0
            for i in range(count-1,len(no)):
                if digit==no[i]:
                    counter+=1
                else:
                    break
            temp=digit
            l.append((counter,int(digit)))
        else:
            continue
    for i in l:
        print(i,end=' ')



