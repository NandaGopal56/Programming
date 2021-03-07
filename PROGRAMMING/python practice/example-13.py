class employee:
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal
    def __repr__(self):
        return '{} {} {}'.format(self.name,self.id,self.sal)

if __name__=='__main__':
    count=int(input('count:'))
    lst=[]
    for _ in range(count):
        name=input('name:')
        id=int(input('id:'))
        sal=int(input('sal:'))
        lst.append(employee(name,id,sal))
    for i in lst:
        print(i)
        print(i.name,i.sal,i.id)