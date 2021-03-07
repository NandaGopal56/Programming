class student:
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal

    def __repr__(self):
        return '{} {} {}'.format(self.name,self.id,self.sal)

    def check(self):
        for i in l:
            print(i.name)
    def fun(self):
        for i in l:
            i=str(i)
            print(i,type(i))

if __name__=='__main__':
    l=[]
    count=int(input('enter count: '))
    for i in range(count):
        name=input('enter name: ')
        id=int(input('enter id: '))
        sal=int(input('enter salary: '))
        l.append(student(name,id,sal))

    for i in range(count):
        print(l[i].name)
        l[i].check()
        l[i].fun()

