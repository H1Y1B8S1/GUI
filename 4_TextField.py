import tkinter as tk

win = tk.Tk()
win.title('Entry box')
win.geometry('500x500')
win.configure(bg='#ffff00')


# when we usign grid onlt use grid. if we use place than grid dont know where to start
text1 = tk.Entry(win).grid(row=1,column=0) #  we can only change width.
text2 = tk.Entry(win).grid(row=2,column=1)
text2 = tk.Entry(win).grid(row=3,column=6)
text2 = tk.Entry(win).grid(row=4,column=0)

win.mainloop()