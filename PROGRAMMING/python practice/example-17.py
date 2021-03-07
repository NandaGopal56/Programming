#!/bin/python3

import math
import os
import random
import re
import sys


class Employee:
    def __init__(self,name,id,age,gender):
        self.name=name
        self.id=id
        self.age=age
        self.gender=gender

class Organisation:
    def __init__(self,oname,employees):
        self.oname=oname
        self.employees=employees
    def addEmployee(self,name,id,age,gender):
        self.name=name
        self.id=id
        self.age=age
        self.gender=gender
        #print('@',name,id,age,gender)
        self.employees.append(Employee(self.name,self.id,self.age,self.gender))

    def getEmployeeCount(self):
        return len(self.employees)

    def findEmployeeAge(self,cid):
        #print("*",cid)
        for j in self.employees:
            #print("id-",j.id)
            if j.id == cid:
                return j.age
        return -1

    def countEmployees(self,cage):
        #print("*",cage)
        count=0
        for i in self.employees:
            if i.age > cage:
                count+=1
        
        return count


if __name__ == '__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(name,id,age,gender)

    id=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))