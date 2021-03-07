class emp:
    def __init__(self,name,id,stream,exp):
        self.name=name
        self.id=id
        self.stream=stream
        self.exp=exp
class check:
    def __init__(self,l):
        for i in l:
            if i.stream=='c' and int(i.exp) >=5:
                print(i.name)

    def select(self,l):
        for i in l:
            if i.stream=='c' and int(i.exp) >=5:
                print(i.name)

if __name__=='__main__':
    l=[]
    for i in range(int(input('enter count: '))):
        name=input('enter name: ')
        id=input('enter id: ')
        stream=input('enter stream: ')
        exp=input('enter experience: ')
        l.append(emp(name,id,stream,exp))

    obj=check(l)
    obj.select(l)