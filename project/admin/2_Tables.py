#"""This program is for add/remove tables."""

import mysql.connector 
myconn = mysql.connector.connect(host = 'localhost',user='root',passwd='',database='shopping')
cur = myconn.cursor()

try:
    userInfo = cur.execute("create table userinfo(name varchar(40) not null,email varchar(30) primary key,password varchar(20) not null,mobile varchar(10),age varchar(3),sex varchar(1),cartvalue int(10) DEFAULT '0')")
    print('done')

except Exception as e:
    print('can not process')
    print(e)

myconn.close()