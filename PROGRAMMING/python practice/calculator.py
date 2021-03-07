
import math
from math import *
from tkinter import *

window=Tk()
window.title("Calculator")
window['bg']='gray34'
window.geometry('407x345')
window.resizable(0,0)

operator=''
temp_operator=''

answer=StringVar()
resultLabel = Entry(window,bd=20, bg="powder blue",textvariable=answer,justify='right')
resultLabel.grid(row=0,column=0,columnspan=7)

print(operator)
answer.set(00.00)


def clicked(a):
    global operator
    print(a,end='')
    operator=operator+str(a)
    answer.set(operator)

def showans():
    try:
        global operator
        ans = str(eval(operator))
        print('\n', ans)
        answer.set(ans)
        operator = ans
    except:
        answer.set('invalid operation')

def clear_all():
    try:
        answer.set(00.00)
        global operator
        global temp
        temp=''
        operator = ''
    except:
        answer.set("math error")

def delete_entry():
    try:
        global operator
        new_operator = ''
        l = len(operator)
        for i in range(l - 1):
            new_operator = new_operator + operator[i]
        operator = new_operator
        answer.set(operator)
    except:
        answer.set("math error")

def point_decimal():
    try:
        global operator
        operator = operator + '.'
        answer.set(operator)
    except:
        answer.set('MATH ERROR')

def calculate_square():
    try:
        global operator
        operator = str(float(operator) * float(operator))
        answer.set(operator)
    except:
        answer.set("MATH ERROR")

def calculate_square_root():
    try:
        global operator
        operator = str(sqrt(float(operator)))
        answer.set(operator)
    except:
        answer.set('MATH ERROR')
def calc_divide_by_x():
    try:
        global operator
        operator = str(1 / float(operator))
        answer.set(operator)
    except:
        answer.set('MATH ERROR')

def calc_logarithm():
    try:
        global operator
        operator = str(math.log(float(operator)))
        answer.set(operator)
    except:
        answer.set('MATH ERROR')

def calc_trigonometry(func):
    try:
        global operator
        operator=str(float(operator)*math.pi/180)

        if func==sine:
            operator=str(math.sin(float(operator)))
            answer.set(operator)
        elif func==cosine:
            operator=str(math.cos(float(operator)))
            answer.set(operator)
        elif func==tan:
            operator = str(math.tan(float(operator)))
            answer.set(operator)
        elif func==cot:
            operator = str(1/math.tan(float(operator)))
            answer.set(operator)
        elif func==sec:
            operator = str(1/math.cos(float(operator)))
            answer.set(operator)
        elif func==cosec:
            operator = str(1/math.sin(float(operator)))
            answer.set(operator)
    except:
        answer.set('enter value first')

def calc_percentile():
    global operator
    answer.set(operator+'%')

    try:
        operator = operator.split('%')
        symbol = ['+', '-', '*', '/']

        operator_list = []

        for expression in operator:
            if expression != '':
                print(expression)

                x = ''
                if len(expression) > 1:
                    for i in range(len(expression) - 1, -1, -1):
                        if expression[i] not in symbol:
                            x = x + expression[i]
                        else:
                            break
                else:
                    x = expression

                x = x[::-1]
                percentage = float(x) / 100
                print(percentage)

                l = []
                for item in expression:
                    l.append(item)

                if len(expression) > 1:
                    for i in range(len(expression) - 1, -1, -1):
                        print(l[i])
                        if expression[i] not in symbol:
                            l[i] = '$'
                        else:
                            break
                else:
                    l[0] = '$'

                for i in range(len(l)):
                    try:
                        l.remove('$')
                    except:
                        print('exception raised:can not remove')

                l.append(percentage)
                expression = ''

                for item in l:
                    expression = expression + str(item)

                print(expression)
                operator_list.append(expression)

        operator = ''.join(operator_list)
        print(operator)
    except:
        answer.set('math error')


def calc_factorial():
    global operator
    try:
        operator = math.factorial(int(operator))
        answer.set(operator)
    except:
        answer.set('math error')

def memory_clear():
    try:
        global temp_operator
        temp_operator=''
    except:
        answer.set('MATH ERROR')
def memory_store():
    try:
        global operator
        global temp_operator
        temp_operator = operator
    except:
        answer.set('MATH ERROR')

def memory_recall():
    try:
        global operator
        global temp_operator
        if temp_operator == '':
            answer.set('memory empty')
        else:
            operator = operator+temp_operator
            answer.set(operator)
    except:
          answer.set('MATH ERROR')
def memory_plus():
    try:
        global operator
        global temp_operator

        if temp_operator != '':
            showans()
            operator=str(int(operator)+int(temp_operator))
            answer.set(operator)
            temp_operator=operator
        else:
            answer.set("memory empty")
    except:
        answer.set('MATH ERROR')
def memory_minus():
    try:
        global operator
        global temp_operator

        if temp_operator != '':
            showans()
            operator = str(int(temp_operator) - int(operator))
            answer.set(operator)
            temp_operator = operator
        else:
            answer.set("memory empty")
    except:
        answer.set('MATH ERROR')
'''===============================================================================
   ================================================================================'''

btn1 = Button(window,bg='cyan',padx=16,pady=16, text="01", command=lambda :clicked(1))
btn1.grid(column=0, row=1)

btn2 = Button(window,bg='cyan',padx=16,pady=16, text="02", command=lambda :clicked(2))
btn2.grid(column=1, row=1)

btn3 = Button(window,bg='cyan',padx=16,pady=16, text="03", command=lambda :clicked(3))
btn3.grid(column=2, row=1)

btn4 = Button(window,bg='cyan',padx=16,pady=16, text="04", command=lambda :clicked(4))
btn4.grid(column=0, row=2)

btn5 = Button(window,bg='cyan',padx=16,pady=16, text="05", command=lambda :clicked(5))
btn5.grid(column=1, row=2)

btn6 = Button(window,bg='cyan',padx=16,pady=16, text="06", command=lambda :clicked(6))
btn6.grid(column=2, row=2)

btn7 = Button(window,bg='cyan',padx=16,pady=16, text="07", command=lambda :clicked(7))
btn7.grid(column=0, row=3)

btn8 = Button(window,bg='cyan',padx=16,pady=16, text="08", command=lambda :clicked(8))
btn8.grid(column=1, row=3)

btn9 = Button(window,bg='cyan',padx=16,pady=16, text="09", command=lambda :clicked(9))
btn9.grid(column=2, row=3)

btn10 = Button(window,bg='cyan',padx=16,pady=15, text="00", command=lambda :clicked(0))
btn10.grid(column=1, row=4)

point=Button(window,bg='powder blue',padx=18,pady=18,text='  . ',command=lambda :point_decimal())
point.grid(column=4,row=2)

'''===========================================================================
   ==========================================================================='''
operator1=Button(window,bg='gainsboro',padx=19,pady=16,text="+",command=lambda :clicked('+'))
operator1.grid(column=3,row=1)

operator2=Button(window,bg='gainsboro',padx=20,pady=16,text="-",command=lambda :clicked('-'))
operator2.grid(column=3,row=2)

operator3=Button(window,bg='gainsboro',padx=20,pady=16,text="*",command=lambda :clicked('*'))
operator3.grid(column=3,row=3)

operator4=Button(window,bg='gainsboro',padx=20,pady=15,text="/",command=lambda :clicked('/'))
operator4.grid(column=3,row=4)

'''===========================================================================
   ==========================================================================='''


'''===========================================================================
   ==========================================================================='''


show=Button(window,bg='red',padx=18,pady=15,text='=',command=lambda :showans())
show.grid(column=2,row=4)

clear=Button(window,bg='red',padx=15,pady=15,text='CE',command=lambda :clear_all())
clear.grid(column=0,row=4)

'''===========================================================================
   ==========================================================================='''

delete=Button(window,bg='powder blue',padx=16,pady=16,text='del',command=lambda :delete_entry())
delete.grid(column=4,row=1)


square=Button(window,bg='powder blue',padx=14,pady=15,text='x^2',command=lambda :calculate_square())
square.grid(column=4,row=3)

square_root=Button(window,bg='powder blue',padx=15,pady=15,text='sqrt',command=lambda :calculate_square_root())
square_root.grid(column=4,row=4)

'''===========================================================================
   ==========================================================================='''

divide_by_x=Button(window,bg='powder blue',padx=14,pady=16.5,text='1/x',command=lambda :calc_divide_by_x())
divide_by_x.grid(column=5,row=1)

logarithm=Button(window,bg='powder blue',padx=18,pady=17,text='ln',command=lambda :calc_logarithm())
logarithm.grid(column=5,row=2)

percentile=Button(window,bg='powder blue',padx=18,pady=16,text='%',command=lambda : calc_percentile())
percentile.grid(column=5,row=3)

factorial=Button(window,bg='powder blue',padx=18,pady=16,text='n!',command=lambda : calc_factorial())
factorial.grid(column=5,row=4)
'''==================================================================================
   =================================================================================='''

sine=Button(window,bg='magenta',padx=16,pady=16,text='sin',command=lambda :calc_trigonometry(sine))
sine.grid(column=0,row=5)

cosine=Button(window,bg='magenta',padx=16,pady=16,text='cos',command=lambda :calc_trigonometry(cosine))
cosine.grid(column=1,row=5)

tan=Button(window,bg='magenta',padx=16,pady=16,text='tan',command=lambda :calc_trigonometry(tan))
tan.grid(column=2,row=5)

cot=Button(window,bg='magenta',padx=16,pady=16,text='cot',command=lambda :calc_trigonometry(cot))
cot.grid(column=3,row=5)

sec=Button(window,bg='magenta',padx=16,pady=16,text='sec',command=lambda :calc_trigonometry(sec))
sec.grid(column=4,row=5)

cosec=Button(window,bg='magenta',padx=10,pady=16,text='cosec',command=lambda :calc_trigonometry(cosec))
cosec.grid(column=5,row=5)


'''==============================================================================================
   ==============================================================================================='''
mc = Button(window,bg='cyan',padx=16,pady=16, text="MC", command=lambda :memory_clear())
mc.grid(column=6, row=1)

mr = Button(window,bg='cyan',padx=16,pady=17,text="MR", command=lambda :memory_recall())
mr.grid(column=6, row=2)

ms = Button(window,bg='cyan',padx=16,pady=16, text="MS", command=lambda :memory_store())
ms.grid(column=6, row=3)

mp = Button(window,bg='cyan',padx=15,pady=16, text="M+", command=lambda :memory_plus())
mp.grid(column=6, row=4)

mm = Button(window,bg='cyan',padx=17,pady=16, text="M-", command=lambda :memory_minus())
mm.grid(column=6, row=5)

'''===========================================================================
   ==========================================================================='''

window.mainloop()