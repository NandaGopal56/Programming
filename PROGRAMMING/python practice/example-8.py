
class first:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def verify(self,lst):
        l=[]
        for i in lst:
            if i.name=='nanda':
                print("first is okay")
        l.append(second(lst))
        for i in l:
            i.check()

class second:
    def __init__(self,lst):
        self.lst=lst
    def check(self):
        l3=[]
        for i in self.lst:
            if i.name=='gopal':
                print("second is good")
        for i in self.lst:
            l3.append(third(i.name,i.id))


class third:
    def __init__(self,name,id):
        self.name2=name
        self.id2=id

        print(self.name2,self.id2,end="\n")

if __name__=='__main__':
    lst=[]
    count=2
    for i in range(count):
        name=input('enter name: ')
        id=int(input('enter id: '))
        lst.append(first(name,id))
    demo_obj=first('',0)
    demo_obj.verify(lst)

    third_obj=third('ngp',150)