from tkinter import *
from MySQLdb import *
def ok():
    conobj=connect('localhost','','')
    curobj=conobj.cursor()
    curobj.execute('create database GUIAPPLICATION')
    curobj.execute('use GUIAPPLICATION')
    curobj.execute('create table signup(uid varchar(30),eid varchar(30),phno varchar(20),var varchar(10),pwd varchar(50)')
    curobj.execute('insert into signup values(" '+uid+get()+' "," '+eid.get()+' "," '+phn.get()+' "," '+var.get()+' "," '+pwd.get()+' ");')
    curobj.close()
    conobj.close()
def display():
    conobj = connect('localhost', '', '')
    curobj = conobj.cursor()
    curobj.execute('use GUIAPPLICATION')
    curobj.execute('select * from signup;')
    record=curobj.fetchall()
    for a,b,c,d,e in record:
        print (a,b,c,d,e)
    curobj.close()
    conobj.close()

def exit():
    root.destroy()

root=Tk()

root.title("GUI Application")

Label(root,text="please signUp here !!!",font=("bold",15),bg="brown",fg="white").pack()

f1=Frame()
Label(f1,text="enter user id",font=("bold",10),bg="grey",fg="white").pack(side=LEFT)
uid=Entry(f1,font=('bold',10),bg='white',fg='blue')
uid.pack(side=RIGHT)
f1.pack()

f2=Frame()
Label(f2,text="enter email id",font=("bold",10),bg="grey",fg="white").pack(side=LEFT)
eid=Entry(f2,font=('bold',10),bg='white',fg='blue')
eid.pack(side=RIGHT)
f2.pack()

f3=Frame()
Label(f3,text="enter phone no.",font=("bold",10),bg="grey",fg="white").pack(side=LEFT)
phn=Entry(f3,font=('bold',10),bg='white',fg='blue')
phn.pack(side=RIGHT)
f3.pack()

f4=Frame()
Label(f4,text="select gender",font=("bold",10),bg="grey",fg="white").pack(side=LEFT)
var=StringVar()
male=Radiobutton(f4,text="male",font=("bold",10),variable=var,value='male')
male.pack(side=RIGHT)
female=Radiobutton(f4,text="female",font=("bold",10),variable=var,value='female')
female.pack(side=RIGHT)
f4.pack()

f5=Frame()
Label(f5,text="enter password",font=("bold",10),bg="grey",fg="white").pack(side=LEFT)
pwd=Entry(f5,font=('bold',10),bg='white',fg='blue')
pwd.pack(side=RIGHT)
f5.pack()

f6=Frame()
ok=Button(f6,text='submit',bg="grey",fg="white",font=("bold",10),command=ok).pack(side=LEFT)
display=Button(f6,text='Display',bg="grey",fg="white",font=("bold",10),command=display).pack(side=RIGHT)
exit=Button(f6,text='Exit',bg="grey",fg="white",font=("bold",10),command=exit).pack(side=RIGHT)
f6.pack()



root.mainloop()




