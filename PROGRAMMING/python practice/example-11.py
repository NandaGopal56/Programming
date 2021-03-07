class student:
    def __init__(self,name,roll,section):
        self.name=name
        self.roll=roll
        self.section=section

    def __repr__(self):
        return '{} {} {}'.format(self.name,self.roll,self.section)

class marks:
    def __init__(self,math,eng,science,l):
        self.math=math
        self.eng=eng
        self.science=science
        self.l=l
    def verify(self):
        total=self.math+self.eng+self.science
        for i in self.l:
            if i.name=='nanda':
                if total >= 30:
                    print('goooooooooood')
                else:
                    print('its okkkkkkkkkk')


class verification:
    def __init__(self,l,count):
        self.count=count
        self.l=l

    def check(self):
        mark=[]
        for i in range(self.count):
            math=int(input("enter math mark:"))
            eng=int(input('enter eng mark:'))
            science=int(input('enter science mark:'))
            mark.append(marks(math,eng,science,self.l))
        for i in mark:
             i.verify()
if __name__=='__main__':
    count=1
    l=[]
    for _ in range(1):
        name='nanda'
        roll=10
        section='A'
        l.append(student(name,roll,section))
    obj=verification(l,count)
    obj.check()
