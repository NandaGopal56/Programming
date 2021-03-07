class employee:
    def __init__(self,name,i,sal):
        self.name=name
        self.id=id
        self.sal=sal

    def increment(self,inc):
        show(l,inc)
        for j in l:
            print(j.name, j.id, j.sal)


class show:
    def __init__(self,l,inc):
        for i in l:
            i.sal=i.sal+(i.sal*inc)/100
        for i in l:
            print(i.name,i.id,i.sal)
if __name__ == '__main__':
    l=[]
    count=1
    inc=10
    for i in range(count):
        name='nanda'
        id='05'
        sal=30000
        l.append(employee(name,id,sal))
    for i in l:
        i.increment(inc)
