import mysql.connector as sql

class signIn:
    
    def __init__(self):
        self.con = sql.connect(host = 'localhost',user='root',passwd='',database='shopping')


    def connect_database(self,username,password):
        flag = False
        #append password and username in the emptey list below for later checkings
        mypassword_queue = []
        sql_query = "SELECT *FROM userinfo WHERE email ='%s' OR mobile = '%s' AND password ='%s'" % (username, username,password)
        mycursor = self.con.cursor()

        try:
            mycursor.execute(sql_query)
            myresults =mycursor.fetchall()
            for row in myresults:
                for x in row:
                    mypassword_queue.append(x)
        except:
            print('error occured')

        if (username and password) in mypassword_queue:
            # print('there is something')
            flag = True
            # print(mypassword_queue)
        else:
            # print('there is no anything')
            flag = False

        self.con.close()
        return mypassword_queue #,flag


# root = signIn()
# #---you must have created a database with choice of your database name for this case it is testing
# #---- the data inside has name as tumusiime and password 1234
# root.connect_database(username='siddharthsinh697@gmail.com',password='123456tfg')