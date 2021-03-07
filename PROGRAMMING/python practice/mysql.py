from MySQLdb import*
conobj=connect('localhost','','')
curobj=conobj.cursor()

#delete database
curobj.execute('drop databse WINTER;')

#create database
curobj.execute('create database WINTER;')

#select database
curobj.execute('use WINTER;')

#create table
curobj.execute('create table info(regno int,fanme varchar(20),address varchar(50));')

#insert record
curobj.execute('insert into info values(1,"raja","bbsr");')
curobj.execute('insert into info (regno,fname) values(2,"nanda");') #insert particular field

#add column
curobj.execute('alter table info add column course varchar(15);')
curobj.execute('alter table info add column lname varchar(15) after fname;')

#update record
curobj.execute('update info set lname="panda",course="python" where regno=1;')
curobj.execute('update info set lname="das",course="java",address="bhubaneswar" where regno=2;')

#delete a record
curobj.execute('delete from info ehere regno=2;')

#fetch all record
curobj.execute('select * from info;')
record=curobj.fetchall()
for regno,fname,lnmae,address,course in record:
    print(regno,fname,lnmae,address,course)

curobj.close()
conobj.close()