import tkinter as tk
from PIL import Image,ImageTk


def menu(user): #list

    """This window will show User details and other Function to go"""

    menuScrn = tk.Tk()
    menuScrn.geometry('1500x800')
    menuScrn.title("SHOPPING")
    # menuScrn.attributes('-fullscreen', True)
    menuScrn.configure(bg='gray')
    #=== icon
    icon = ImageTk.PhotoImage(Image.open('C:\SINH\☆Work☆\Projects\Shopping\image\icon.png'))
    menuScrn.wm_iconphoto(False,icon)
    #=== bf image
    BGimg = ImageTk.PhotoImage(Image.open('C:\SINH\☆Work☆\Projects\Shopping\image\\bg3.jpg'))
    bglabel = tk.Label(menuScrn,image=BGimg).pack()

    #--------------------------- Labels ----------------------------------#

    greet = tk.Label(menuScrn,text=f'> Hello {user[0]}, well come to \nshopping.', fg='#000000',font= ('Monaco',25))
    greet.place(x=300,y=50)
    l1 = tk.Label(menuScrn,text=f'Account details', fg='#000000',font= ('Monaco bold',40))
    name = tk.Label(menuScrn,text=f'Name: {user[0].upper()}', fg='#000000',font= ('Monaco bold',30))
    email = tk.Label(menuScrn,text=f'Email: {user[1]}', fg='#000000',font= ('Monaco bold',30))
    password = tk.Label(menuScrn,text=f'Password: {user[2]}', fg='#000000',font= ('Monaco bold',30))
    mobile = tk.Label(menuScrn,text=f'Mobile no: {user[3]}', fg='#000000',font= ('Monaco bold',30))
    age = tk.Label(menuScrn,text=f'Age: {user[4]}', fg='#000000',font= ('Monaco bold',30))
    gender = tk.Label(menuScrn,text=f'Gender: {user[5].upper()}', fg='#000000',font= ('Monaco bold',30))
    # cartValue = tk.Label(menuScrn,text=f'Your cart value {user[-1]}$.', fg='#000000',font= ('Monaco',20))
    # cartValue.place(x=250,y=100)


    width = 100
    height = 100
    def callback():
        pass

    #===user===#
    def accountdetails():
        userB.place_forget()
        cartB.place_forget()
        SlistB.place_forget()
        greet.place_forget()
        l1.place(x=50,y=50)
        name.place(x=100,y=200)
        email.place(x=100,y=300)
        password.place(x=100,y=400)
        mobile.place(x=100,y=500)
        age.place(x=100,y=600)
        gender.place(x=100,y=700)
        homeB.place(x=1350,y=650)
    

    def Home():
        userB.place(x=100,y=150)
        cartB.place(x=100,y=300)
        homeB.place(x=100, y=600)
        SlistB.place(x=100,y=450)
        l1.place_forget()
        name.place_forget()
        email.place_forget()
        password.place_forget()
        mobile.place_forget()
        age.place_forget()
        gender.place_forget()

        

    user = Image.open("C:\SINH\☆Work☆\Projects\Shopping\image\\account.png")
    user = user.resize((width,height),Image.Resampling.LANCZOS)
    photoImg2 = ImageTk.PhotoImage(user)
    userB = tk.Button(menuScrn,image=photoImg2,command=accountdetails)
    userB.place(x=150,y=150)


    #===cart===#
    cart = Image.open("C:\SINH\☆Work☆\Projects\Shopping\image\\icon.png")
    cart = cart.resize((width,height),Image.Resampling.LANCZOS)
    photoImg3 = ImageTk.PhotoImage(cart)
    cartB = tk.Button(menuScrn,image=photoImg3,command=callback)
    cartB.place(x=150,y=300)


    #===shopping list===#
    Slist = Image.open("C:\SINH\☆Work☆\Projects\Shopping\image\list.png")
    Slist = Slist.resize((width,height),Image.Resampling.LANCZOS)
    photoImg4 = ImageTk.PhotoImage(Slist)
    SlistB = tk.Button(menuScrn,image=photoImg4,command=callback)
    SlistB.place(x=150,y=450)


    #===home===#
    home = Image.open("C:\SINH\☆Work☆\Projects\Shopping\image\home.png")
    home = home.resize((width,height), Image.Resampling.LANCZOS)
    photoImg =  ImageTk.PhotoImage(home)
    homeB = tk.Button(menuScrn,image=photoImg, command=Home)
    homeB.place(x=150, y=600)



    def exit():
        menuScrn.destroy()
    quitB = tk.Button(menuScrn,text='exit',bg='#0C9E00', fg='#ffffff',font= ('',16),command=menuScrn.quit)
    quitB.place(x=1440,y=750)

    menuScrn.mainloop()



# menu(['hello',2000,123,123,'no','m'])