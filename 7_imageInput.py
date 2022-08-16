from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

Window = tk.Tk()
Window.geometry('1200x1000')
frame = tk.Frame(
    Window, width=1200, height=1000
)
frame.pack()
img = ImageTk.PhotoImage(Image.open(
    "C:\SINH\☆SINH☆\documents\IMG-20210203-WA0020.jpg"))
l1 = tk.Label(frame, image=img)
l1.place(x=250, y=250)
Window.mainloop()
