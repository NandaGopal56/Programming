class emp:
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal

    def check(self,ch):
        self.ch=ch
        if self.name=='nanda gopal' and self.sal >=self.ch:
            print('perfect')

class student:
    def calculate(self,l):
        self.l=l
        for i in self.l:
            print(i.name)

if __name__=='__main__':
    l=[]
    for i in range(1):
        name='nanda gopal'
        id=15
        sal=500000
        l.append(emp(name,id,sal))
    ch=500
    for i in l:
        i.check(ch)
    obj=student()
    obj.calculate(l)