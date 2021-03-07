import mysql.connector
from pip._vendor.distlib import database

mydb=mysql.connector.connect(host='localhost',
                             user='gopal',
                             passwd='123456',
                             database='mydatabase'
                             )


#If the database does not exist, you will get an error

