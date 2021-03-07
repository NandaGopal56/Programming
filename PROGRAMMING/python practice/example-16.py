class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def check(self,inc):
        self.salary=self.salary+inc
class organisation:
    def __init__(self,l):
        self.l=l
    def verify(self,inc,name):
        self.inc=inc
        self.name=name
        final=[]
        for i in self.l:
            if i.name==self.name:
                i.check(self.inc)
                final.append(i)
        return final


if __name__ == '__main__':
    count=int(input('enter count:'))
    l=[]
    for i in range(count):
        name=input('enter name:')
        id=int(input('enter id:'))
        salary=int(input('enter salary:'))
        l.append(employee(name,id,salary))
    obj=organisation(l)
    final=obj.verify(int(input('enter increment:')),input('enter name'))
    print(final)
    for i in final:
        print(i.name,i.salary)