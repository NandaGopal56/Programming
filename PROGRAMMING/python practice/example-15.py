class employee:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def verify(self):
        print(self.x)

class calculate:
    def __init__(self,l):
       self.l=l
    def check(self,inc):
        self.inc=inc
        for i in self.l:
            i.x=i.x+self.inc
            print(i.x)


if __name__ == '__main__':
    l=[]
    x=10
    y=20
    l.append(employee(x,y))
    o=calculate(l)
    o.check(100)
    for i in l:
        i.verify()