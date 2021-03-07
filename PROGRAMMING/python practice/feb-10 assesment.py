
#feb-10 assesment code

class employee:
    def __init__(self,id,name,role,salary):
        self.id=id
        self.name=name
        self.role=role
        self.salary=salary

    def increase_salary(self,inc):
        self.salary+=self.salary*(inc/100)
class organisation:
    def __init__(self,org_name,emp_list):
        self.org_name=org_name
        self.emp_list=emp_list
    def calculate_salary(self,role,percentage):
        self.role=role
        self.percentage=percentage
        result=[]
        for i in self.emp_list:
            if i.role==self.role:
                i.increase_salary(percentage)
                result.append(i)
        return result
if __name__ == '__main__':
    count=int(input('enter count:'))
    l=[]
    for i in range(count):
        id=int(input('enter id:'))
        name=input('enter name:')
        role=input('enter role:')
        salary=int(input('enter salry:'))
        l.append(employee(id,name,role,salary))
    o=organisation('xyz',l)
    role=input('enter role:')
    percentage=int(input('enter percentage:'))
    result=o.calculate_salary(role,percentage)
    for i in result:
        print(i.name)
        print(i.salary)

'''

#feb-10 assesment my code

class employee:
    def __init__(self,id,name,role,salary):
        self.id=id
        self.name=name
        self.role=role
        self.salary=salary

    def increase_salary(self,inc):
        self.inc=inc
class demo:
    def __init__(self,ename,esal):
        self.ename=ename
        self.esal=esal
class organisation:
    def __init__(self,org_name,emp_list):
        self.org_name=org_name
        self.emp_list=emp_list
    def calculate_salary(self,role,percentage):
        self.role=role
        self.percentage=percentage
        result=[]
        for i in self.emp_list:
            if i.role==self.role:
                i.salary=i.salary+i.salary*(percentage/100)
                result.append(demo(i.name,i.salary))
        return result
if __name__ == '__main__':
    count=int(input('enter count:'))
    l=[]
    for i in range(count):
        id=int(input('enter id:'))
        name=input('enter name:')
        role=input('enter role:')
        salary=int(input('enter salry:'))
        l.append(employee(id,name,role,salary))
    o=organisation('xyz',l)
    role=input('enter role:')
    percentage=int(input('enter percentage:'))
    result=o.calculate_salary(role,percentage)
    for i in result:
        print(i.ename)
        print(i.esal)
'''