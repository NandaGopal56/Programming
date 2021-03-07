studentDB={}

def insertstudent(regno,name=None,*marks,**info):
    print(regno,name,marks,info)
    studentDB[regno]={'name':name,'marks':marks,'info':info}

def plus2():
    names=[]
    for reg in studentDB:
        if len(studentDB[reg]['marks'])>=2:
            names.append(studentDB[reg]['name'])
    return names

def maxplus2():
    maxmark=0
    maxname=None
    for reg in studentDB:
        if len(studentDB[reg]['marks'])>=2:
            if studentDB[reg]['marks'][1]>maxmark:
                maxmark=studentDB[reg]['marks'][1]
                maxname=studentDB[reg]['name']
    return maxname

def main():
    insertstudent('lit01')
    insertstudent('lit02',name='raja')
    insertstudent('lit03','rani',89.5,99)
    insertstudent('lit04','rajani',89.5,98,68)
    insertstudent('lit05','rajanikant',89.5,88,68,86,78,addr='bbsr',pno=606060)


    print(studentDB)
    print(plus2())
    print(maxplus2())

main()

