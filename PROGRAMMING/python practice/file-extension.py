def find_extension(filename):
    temp=''
    filename = filename[::-1]

    for i in filename:
        if i == '.':
            break
        else:
            temp += i

    temp = temp[::-1]

    print(temp)



find_extension('first.pdf')
find_extension('second.docx')
find_extension('third.jpeg')
find_extension('second.xml')
find_extension('second.docs')
find_extension('kckabsk.hcbjha')