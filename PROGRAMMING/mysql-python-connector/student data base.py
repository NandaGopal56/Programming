import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='mydatabase')

mycursor=mydb.cursor()


#mycursor.execute('DROP TABLE Student_database')
#mycursor.execute('CREATE TABLE Student_database(rollno int(10),name VARCHAR(20),type CHAR(5),marks INTEGER(10))')

def entry():
    rollno=int(input('enter the roll mo:'))
    name=input('enter name:')
    name=name.capitalize()
    type=input('enter type(H/D):')
    type=type.upper()
    marks=int(input('enter marks:'))
    sql='insert into Student_database(rollno,name,type,marks)value(%s,%s,%s,%s)'
    val=(rollno,name,type,marks)
    mycursor.execute(sql,val)
    mydb.commit()

def update():
    rno=input('\n\nEnter Roll NO:')
    marks=input('enter marks to be updated:')
    sql='update Student_database set marks=%s where rollno=%s'%(marks,rno,)
    mycursor.execute(sql)
    mydb.commit()

def search(n):
    sql='select *from Student_database where rollno=%s'%(n,)
    mycursor.execute(sql)
    #mydb.commit()
    result=mycursor.fetchall()
    for i in result:
        print(i)

def show_all():
    sql='select * from Student_database'
    mycursor.execute(sql)
    result=mycursor.fetchall()
    for i in result:
        print(i)

def delete():
    rno=int(input('enter roll no to delete data:'))
    sql='delete from student_database where rollno=%s'%(rno,)
    mycursor.execute(sql)
    mydb.commit()
while True:
    print(60*'=')
    print(""" MAIN MENU
    1.student data entry
    2.update marks
    3.search students
    4.all students record
    5.delete student record
    6.exit
    """)
    ch = int(input('enter your choice:'))
    try:
        if ch == 1:
            entry()
            print('data entered successfully')
        elif ch == 2:
            update()
            print('arks updated successfully')
        elif ch == 3:
            rno = input('enter rollno:')
            search(rno)
        elif ch == 4:
            show_all()
        elif ch == 5:
            delete()
            print('record deleted successfully')
        elif ch == 6:
            break
        else:
            print('invalid choice')
    except:
        print('error occured')
    print(60*'=')
