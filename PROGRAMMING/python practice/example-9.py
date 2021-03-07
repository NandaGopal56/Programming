#!/bin/python3

import math
import os
import random
import re
import sys



#Enter your code here. Read input from STDIN. Print output to STDOUT
class Student:
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.marks=marks
        self.name=name
    def calculate_percentage(self):
        total=0
        c=0
        for i in marks:
            total=total+i
            c=c+1
        
        p=int(total/c)
        return p
    
    def find_grade(self):
        G=self.calculate_percentage()
        for value, grade in (80, "A"), (70, "B"), (60, "C"), (50, "D"):
            if G >= value:
                return grade
        else:
            return "F"




if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input('enter the marks:')))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())
