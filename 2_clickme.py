from tkinter import *
import tkinter as tk

Window = tk.Tk()
Window.title("Click me")
Window.geometry('600x600')
Window.configure(bg='#ffff00')


def w():
    global l1
    l1= tk.Label(Window,text="PYTHON CLASS",bg='#ffff00')
    l1.place(x=250,y=250)
def c():
    global l1
    l1.destroy()


b1 = tk.Button(Window,text="Click me",command=w).place(x=250,y=40)
b2 = tk.Button(Window,text="clear",command=c).place(x=250,y=520)
Window.mainloop()