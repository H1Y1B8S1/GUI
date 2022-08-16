import tkinter as tk 
from tkinter import *
from tkinter import messagebox

windos = tk.Tk()
windos.title("1st GUI")
windos.geometry('750x250')
windos.configure(bg='yellow')


l1 = tk.Label(windos,text="NAME",bg='#fff044',font='bold,12').grid(row=0,column=0)
global enter1 
enter1= tk.Entry(windos,width=100)
enter1.grid(row=0,column=1)

def Print():
    a = enter1.get()
    print(a)
    global l2
    l2 = tk.Label(windos,text=a,bg='#ff00ff',font='bold,12')
    l2.grid(row=3,column=1)

def clear():
    global l2,enter1
    l2.destroy()
    # will also clear text in input box
    # enter1.delete(0,END)    # END only works with *
    enter1.delete(0,'end')

def ex():
    d= messagebox.askquestion('quit','DO you want to quit?')
    if d == 'yes':
        windos.destroy()


b1 = tk.Button(windos,text='Search',width=8,bg='#f0f044',font='bold,32',command=Print).grid(row=1,column=1)
b2 = tk.Button(windos,text='Clear',width=8,bg='#f0f044',font='bold,32',command=clear).grid(row=2,column=1)
B3 = tk.Button(windos,text='EXIT',command=ex).grid(row=2,column=2,)


windos.mainloop()