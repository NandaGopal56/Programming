def count_substring(string, sub_string):
    s=len(sub_string)
    m=0
    counter=0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            k=i
            for j in range(0,s):
                if k < len(string):
                    if string[k]==sub_string[j]:
                        print(k, '2nd index', j)
                        k+=1
                        m+=1

            if m==s:
                print('yes  one match found')
                i-=1
                counter+=1
        m = 0
    return counter

if __name__ == '__main__':
    string = 'ABCDCDCDCDC'
    sub_string = 'CDC'

    count=count_substring(string, sub_string)
    print('repetation of sub_string in the string is=',count)