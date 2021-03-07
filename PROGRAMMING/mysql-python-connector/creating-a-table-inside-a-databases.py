import mysql.connector

mydb=mysql.connector.connect(host='localhost',
                             user='gopal',
                             passwd='123456',
                             database='mydatabases'
                             )

mycursor=mydb.cursor()

mycursor.execute('CREATE TABLE customers(name VARCHAR(255) ,adress VARCHAR(255))')