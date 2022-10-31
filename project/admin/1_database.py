from mysql.connector import connect

database = connect(host='localhost',user='root',passwd="")
cursor = database.cursor()
try:
    cursor.execute("create database shopping")
    print('database created')
except Exception as e:
    print(e)

database.close()