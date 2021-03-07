import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='gopal',passwd='123456')

print(mydb)