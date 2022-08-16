import tkinter as tk

display = tk.Tk()
display.geometry('600x600')
display.configure(bg='#ffff00')


def add():
    global l1
    x = int(input('enter your 1st num: '))
    y = int(input('enter your 2nd num: '))
    l1 = tk.Label(display,text=f'> Addition of {x} and {y} is {x+y}',fg='red',bg='#ffff00')
    l1.place(x=220,y=520)


def mul():
    global l1
    x = int(input('enter your 1st num: '))
    y = int(input('enter your 2nd num: '))
    l1 = tk.Label(display,text=f'> Multiplication of {x} and {y} is {x*y}',fg='red',bg='#ffff00')
    l1.place(x=220,y=520)


def div():
    global l1
    x = int(input('enter your 1st num: '))
    y = int(input('enter your 2nd num: '))
    l1 = tk.Label(display,text=f'> Division of {x} and {y} is {x/y}',fg='red',bg='#ffff00')
    l1.place(x=220,y=520)

def sub():
    global l1
    x = int(input('enter your 1st num: '))
    y = int(input('enter your 2nd num: '))
    l1 = tk.Label(display,text=f'> Subtraction of {x} and {y} is {x-y}',fg='red',bg='#ffff00')
    l1.place(x=220,y=520)


def clear():
    global l1
    l1.destroy()

title = tk.Label(display,text='Calculation',font='bold,32',bg='#ffff00',fg='black').pack()
add = tk.Button(display,text='+',command=add,height=3,width=8).place(x=270,y=120)
mul = tk.Button(display,text='x',command=mul,height=3,width=8).place(x=150,y=240)
div = tk.Button(display,text='/',command=div,height=3,width=8).place(x=390,y=240)
sub = tk.Button(display,text='-',command=sub,height=3,width=8).place(x=270,y=360)
clear = tk.Button(display,text="CLEAR",command=clear,height=3,width=8).place(x=270,y=240)

display.mainloop()