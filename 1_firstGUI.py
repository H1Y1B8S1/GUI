import tkinter as tk

window = tk.Tk()
window.title("MY GUI")

window.geometry('600x600')  # changing aspect ratio acordingly

window.configure(bg='#ffff00')
# window.configure(bg='red') # use color name or color code

# title label
label1 = tk.Label(window, text='Enter your details',
                  bg='#ffff00', fg='#0000ff').place(x=250, y=10)
# label for user name
userName = tk.Label(window, text='User Name :').place(x=40, y=60)
# labe for user password
userPassword = tk.Label(window, text='User Password :').place(x=40, y=100)


def fun():
    print("hello sir enter your name")
def fun2():
    print("hello sir enter your password")

# creating buttons
useNameB = tk.Button(window,text='Enter here',command=fun).place(x=130,y=60)
usePasswordB = tk.Button(window,text='Enter here',command=fun2).place(x=130,y=100)





window.mainloop()
