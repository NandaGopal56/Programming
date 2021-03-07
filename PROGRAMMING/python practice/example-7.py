class employee:
    def __init__(self,name,id,sal):
        self.name1=name
        self.id1=id
        self.sal1=sal
    def __repr__(self):
        return '{} {} {}'.format(self.name1,self.id1,self.sal1)
    def check(self,lst):
        self.lst=lst
        for i in self.lst:
            print(i.sal1)
            if i.sal1 > 500:
                return 'okay'

class salary:
    def __init__(self,lst):
        self.lst=lst

    def verify(self):
        for i in self.lst:
            if i.name1=='nanda':
                print('name is okay')


    def __repr__(self):
        for i in self.lst:
            return '{} {} {}'.format(i.name1,i.id1,i.sal1)

class student:
    def __init__(self,name,rn):
        self.name=name
        self.rn=rn

class test:
    def testify(self,lst):
        self.lst=lst
        l=[]
        for i in self.lst:
            l.append(student(i.name1,i.id1))
        for i in l:
            print(i.name,i.rn)


if __name__=='__main__':
    lst=[]
    count=1
    for i in range(count):
        name='nanda'
        id=101
        sal=100000
        lst.append(employee(name,id,sal))

    demo_obj=employee('a',0,0)
    print(demo_obj)
    res=demo_obj.check(lst)
    print(res)

    salary_obj=salary(lst)
    print(salary_obj)
    result=salary_obj.verify()

    student_obj=test()
    student_obj.testify(lst)
