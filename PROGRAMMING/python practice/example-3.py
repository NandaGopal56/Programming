class first:
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal

    def random(self):
        print(self.name)
    def __repr__(self):
        return ('{} {} {}').format(self.name,self.id,self.sal)

class second:
    def __init__(self,l):
        self.l=l
        print(self.l)
        for k in self.l:
            print(k.name,k.id,k.sal)

if __name__=='__main__':
    l=[]
    for i in range(int(input('enter count: '))):
        name=input('enter name: ')
        id=int(input('enter id: '))
        sal=int(input('enter salary: '))
        l.append(first(name,id,sal))
    for i in l:                                     #for i in range(count):
        i.random()                                  #       l[i].random()
    obj=second(l)


