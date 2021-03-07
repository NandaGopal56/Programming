class student:
    def __init__(self,name):
        self.name=name

    def check(self,ch):
        m = []
        self.ch=ch
        print(self.ch)
        m.append(self.ch)
        print(m)

class employee:
    def __init__(self,name2,l):
        self.name2=name2
        self.l=l
        for i in self.l:
            i.check('good')


if __name__=='__main__':
    l=[]
    k=[]
    for i in range(1):
        name='nanda'
        l.append(student(name))
    for i in range(1):
        name2='gopal'
        k.append(employee(name2,l))