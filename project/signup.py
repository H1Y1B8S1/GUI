import tkinter as tk
from PIL import ImageTk,Image
from tkinter import Checkbutton,messagebox,END
from mysql.connector import connect


### loging screen
def signUp():
    signUpWin = tk.Toplevel()
    signUpWin.title("New account creation")
    signUpWin.geometry('900x660')
    signUpWin.resizable(False,False) #it will make fix size window so no maximize
    # signUpWin.config(bg='black')

    ### icon
    icon = Image.open('C:\SINH\☆Work☆\Projects\Shopping\image\icon2.png')
    photo = ImageTk.PhotoImage(icon)
    signUpWin.wm_iconphoto(False, photo)
    ### bg-image
    BGimg = ImageTk.PhotoImage(Image.open('C:\SINH\☆Work☆\Projects\Shopping\image\\bg2.png'))
    label =tk.Label(signUpWin, image = BGimg)
    label.pack()

    ### labels and entries for user details
    tk.Label(signUpWin,text='Account information',bg='#000000', fg='#ffffff',font= ('bold',18)).place(x=10,y=10 )
    tk.Label(signUpWin, text='Name:',bg='#FBEAC5', fg='#000000',font='bold,18').place(x=37, y=60)
    tk.Label(signUpWin, text='Email:',bg='#FBEAC5', fg='#000000',font='bold,18').place(x=40, y=120)
    tk.Label(signUpWin, text='Password:',bg='#FBEAC5', fg='#000000',font='bold,18').place(x=10, y=180)
    tk.Label(signUpWin, text='Password Confirm:',bg='#FBEAC5', fg='#000000',font='bold,18').place(x=10, y=240)
    tk.Label(signUpWin, text='Mobile:',bg='#FBEAC5', fg='#000000',font='bold,18').place(x=34, y=300)
    tk.Label(signUpWin, text='Age:',bg='#FBEAC5', fg='#000000',font='bold,18').place(x=53, y=360)
    tk.Label(signUpWin, text='Sex:',bg='#FBEAC5', fg='#000000',font='bold,18').place(x=53, y=420)
    ### all user entries
    nameE = tk.Entry(signUpWin,width= 50, fg='#B68029',font='Arial,18')
    nameE.place(x=110, y=60)
    emailE = tk.Entry(signUpWin, width= 50, fg='#B68029',font='Arial,18')
    emailE.place(x=110, y=120)
    passwordE = tk.Entry(signUpWin, width= 50, fg='#B68029',font='Arial,18')
    passwordE.place(x=110, y=180)
    passwordRE = tk.Entry(signUpWin, width= 45, fg='#B68029',font='Arial,18')
    passwordRE.place(x=200, y=240)
    mobileE = tk.Entry(signUpWin, width= 50, fg='#B68029',font='Arial,18')
    mobileE.place(x=110, y=300)
    ageE = tk.Entry(signUpWin, width= 50, fg='#B68029',font='Arial,18')
    ageE.place(x=110, y=360)
    sexE = tk.Entry(signUpWin, width= 50, fg='#B68029',font='Arial,18')
    sexE.place(x=110, y=420)

    def Final():

        name = nameE.get()
        email = emailE.get()
        password = passwordE.get()
        retypeP = passwordRE.get()
        mobile = mobileE.get()
        age = ageE.get()
        sex = sexE.get()
        if name and email and password and mobile:

            if password == retypeP:
                flag = False  # for already exist

                db = connect(host = 'localhost',user='root',passwd='',database='shopping')
                cur = db.cursor()
                sql = 'insert into userinfo(name,email,password,mobile,age,sex) values(%s,%s,%s,%s,%s,%s)'
                value = (name,email,password,mobile,age,sex)
                try:
                    cur.execute(sql,value)
                    db.commit()
                    print('data inserted')
                except Exception as e:
                    flag = True # exist

                db.close()

                if flag ==True:
                    tk.Label(signUpWin,text='This account already exists with this email address try loging.', fg='#000000',font= ('Monaco',10)).place(x=10,y=600)
                else:
                    tk.Label(signUpWin,text='your account has been created successfully. you can now log in with your email/mobile and password.', fg='#000000',font= ('Monaco',10)).place(x=10,y=600)
                    nameE.delete(0, END)
                    emailE.delete(0, END)
                    passwordE.delete(0, END)
                    passwordRE.delete(0,END)
                    mobileE.delete(0, END)
                    ageE.delete(0, END)
                    sexE.delete(0, END)
            else:
                tk.Label(signUpWin,text='Your passwords are not matching.', fg='#000000',font= ('Monaco',10)).place(x=10,y=600)


        else:
            tk.Label(signUpWin,text='Name,Email,password and Mobile is compulsory to fill.', fg='#000000',font= ('Monaco',10)).place(x=10,y=600)



    submitB = tk.Button(signUpWin,text='Submit',bg='#0C9E00', fg='#ffffff',font= ('',16),command=Final)
    submitB.place(x=350,y=500)

    ### Exit screen to main manu.
    def quit():
        # msg = messagebox.askquestion('Exit','DO you want to go back without saving?')
        # if msg == 'yes':
        signUpWin.destroy()
    quitBut = tk.Button(signUpWin,text='Home',command=quit,bg='#0C9E00', fg='#ffffff',font= ('',16)).place(x=550,y=500)

    signUpWin.mainloop()
