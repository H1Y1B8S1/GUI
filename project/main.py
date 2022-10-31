import tkinter as tk
from PIL import ImageTk,Image
from tkinter import Checkbutton,messagebox,END
from mysql.connector import connect

def logWindow():

    global list1
    list1 = []
    loginWin = tk.Tk()
    loginWin.title("SHOPPING")
    loginWin.geometry('900x660')
    loginWin.resizable(False,False) #it will make fix size window so no maximize
    ### icon
    icon = Image.open('C:\SINH\☆Work☆\Projects\Shopping\image\icon.png')
    photo = ImageTk.PhotoImage(icon)
    loginWin.wm_iconphoto(False, photo)
    ### bg-image
    BGimg = ImageTk.PhotoImage(Image.open('C:\SINH\☆Work☆\Projects\Shopping\image\\bg.jpg'))
    label =tk.Label(loginWin, image = BGimg)
    label.pack()

    ### labels
    label1 = tk.Label(loginWin,text='Welcome to your account',bg='#F6F7F8', fg='#000000',font= ('Monaco',20)).place(x=90,y=310 )
    uName = tk.Label(loginWin, text='User ID :',bg='#9BF7BF', fg='#000000',font='bold,12').place(x=90, y=370)
    uPswd = tk.Label(loginWin, text='Password :',bg='#9BF7BF', fg='#000000',font='bold,12').place(x=90, y=410)

    ### password cheak box functions
    def show():
        uPswd.configure(show='')
        checkBox.configure(command=hide, text='hide password')
    def hide():
        uPswd.configure(show='*')
        checkBox.configure(command=show, text='show password')

    userE = tk.Entry(loginWin, width= 50, fg='#B68029',font='Arial,12')
    userE.place(x=200, y=370)
    uPswd = tk.Entry(loginWin, width= 50,fg='#B68029',font='bold,12',show='*')
    uPswd.place(x=200, y=410)
    checkBox = Checkbutton(loginWin, text='show password',command=show)
    checkBox.place(x=200,y=440)
    
    
    from signin import signIn 
    def sign():
        userid = userE.get()
        password =uPswd.get()
        if userid and password:
            root = signIn()
            global list1 #signIn will return user's details as a list
            list1 = root.connect_database(userid,password) 
            if list1:
                # print(list1)
                loginWin.destroy()
            else:
                tk.Label(loginWin,text='Invalid UserId/Password', fg='#000000',font= ('Monaco',20)).place(x=250,y=600)
        else:
            tk.Label(loginWin,text='Enter your UserId/Password', fg='#000000',font= ('Monaco',20)).place(x=250,y=600)
   
    signINB = tk.Button(loginWin,text='Log In',bg='#0C9E00', fg='#ffffff',font= ('',16),command=sign)
    signINB.place(x=250,y=500)

    from signup import signUp
    signUPL = tk.Label(loginWin,text='If you dont have an account,You can create here.',font=('bold',10)).place(x=450,y=475)
    signUPB = tk.Button(loginWin,text='Sign UP',bg='#0C9E00', fg='#ffffff',font= ('',16),command=signUp)
    signUPB.place(x=550,y=500)

    ### Exit screen
    def quit():
        msg = messagebox.askquestion('Exit','DO you want to EXIT?')
        if msg == 'yes':
            loginWin.destroy()

    quitBut = tk.Button(loginWin,text='QUIT',command=quit,bg='#F32B2B').place(x=840,y=620)
    loginWin.mainloop()
    return list1


userDlist = logWindow()
# print(userDlist)

import manu1
if userDlist:
    manu1.menu(userDlist)
