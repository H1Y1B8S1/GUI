import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title("INFI DATA")
window.geometry("400x400")
window.configure(background='blue')
l1=tk.Label(window,text="NAME")
l1.grid(row=2,column=0)
global text1,da,hra
text1=tk.Entry(window)
text1.grid(row=2,column=1)



def name():
    global text1
    text = text1.get()

    if text=="ibrahim":
        global l2
        l2 = tk.Label(window, text='''NAME:Ibrahim
                                Employee id:001
                               Designation:MANAGER
                               Salary     :40000''')
        l2.grid(row=5, column=1)
    elif text=="ali":
        l2 = tk.Label(window, text='''NAME:Ali
                                   Employee id:002
                                  Designation:ASSISTANT MANAGER
                                  Salary     :20000''')
        l2.grid(row=5, column=1)
    elif text=="mohammad":
         l2 = tk.Label(window, text='''NAME:Mohammad
                               Employee id:003
                                Designation:SUPERVISOR
                                 Salary     :10000''')
         l2.grid(row=5, column=1)
    else:
        l2 = tk.Label(window, text='''Invaid input
        data not found''')
        l2.grid(row=5, column=1)

def hra():
    global text,l2,hra
    l2.destroy()

    if text=="ibrahim":
        l2 = tk.Label(window, text=0.2*40000)
        l2.grid(row=5, column=1)
        hra = 0.2*40000
    elif text=="ali":
        l2 = tk.Label(window, text=0.2 * 20000)
        l2.grid(row=5, column=1)
        hra = 0.2 * 20000
    elif text=="mohammad":
        l2 = tk.Label(window, text=0.2 * 10000)
        l2.grid(row=5, column=1)
        hra = 0.2 * 10000
    else:
        print("error")
def da():
    global text, l2,da
    l2.destroy()

    if text == "ibrahim":
        l2 = tk.Label(window, text=0.4* 40000)
        l2.grid(row=5, column=1)
        da = 0.4*40000
    elif text == "ali":
        l2 = tk.Label(window, text=0.4 * 20000)
        l2.grid(row=5, column=1)
        da = 0.4 * 20000
    elif text == "mohammad":
        l2 = tk.Label(window, text=0.4 * 10000)
        l2.grid(row=5, column=1)
        da = 0.4 * 10000
    else:
        print("error")
def basicsalary():
    global text, l2,da,hra
    l2.destroy()

    if text == "ibrahim":
        l2 = tk.Label(window, text=40000-da-hra)
        l2.grid(row=5, column=1)
    elif text == "ali":
        l2 = tk.Label(window, text=20000-da-hra)
        l2.grid(row=5, column=1)
    elif text == "mohammad":
        l2 = tk.Label(window, text=10000-da-hra)
        l2.grid(row=5, column=1)
    else:
        print("error")

def clear():
    global text1,l2
    text1.delete(0,END)
    l2.destroy()


b1=tk.Button(window,text="search",command=name)
b1.grid(row=2,column=2)
b2=tk.Button(window,text="clear",command=clear)
b2.grid(row=3,column=1)
b3=tk.Button(window,text="clear",command=clear)
b3.grid(row=4,column=3)
b6=tk.Button(window,text="BASIC SALARY",command= basicsalary)
b6.grid(row=7,column=0)
b4=tk.Button(window,text="HRA",command=hra)
b4.grid(row=5,column=0)
b5=tk.Button(window,text="DA",command=da)
b5.grid(row=6,column=0)




window.mainloop()

