from tkinter import (Tk, Label, Entry, Button, StringVar)
from tkinter import (LEFT, RIGHT)

my_app = Tk(className="Kalkulator")

L1 = Label(my_app, text="Angka 1")
L1.grid(row=0, column=0, sticky="w")

str1 = StringVar(value="0")
E1 = Entry(my_app, textvariable=str1)
E1.grid(row=0, column=2, columnspan=5)

L2 = Label(my_app, text="=")
L2.grid(row=0, column=1, sticky="w")

L3 = Label(my_app, text="Angka 2")
L3.grid(row=1, column=0, sticky="w")

str3 = StringVar(value="0")
E3 = Entry(my_app, textvariable=str3)
E3.grid(row=1, column=2, columnspan=5)

L4 = Label(my_app, text="=")
L4.grid(row=1, column=1, sticky="w")

L5 = Label(my_app, text="result")
L5.grid(row=4, column=0, sticky="w")

L6 = Label(my_app, text="=")
L6.grid(row=4, column=1, sticky="w")

L7 = Label(my_app, text=" ")
L7.grid(row=4, column=2, sticky="w")

def tambah():
    a=float(str1.get())
    b=float(str2.get())
    result=a+b
    L7.config(text=result)

def kurang():
    a=float(str1.get())
    b=float(str2.get())
    result=a-b
    L7.config(text=result)

def bagi():
    a=float(str1.get())
    b=float(str2.get())
    result=a/b
    L7.config(text=result)

def kali():
    a=float(str1.get())
    b=float(str2.get())
    result=a*b
    L7.config(text=result)

B1 = Button(my_app, text="+", command=tambah)
B1.grid(row=2, column=0)

B2 = Button(my_app, text="-", command=kurang)
B2.grid(row=2, column=1)

B3 = Button(my_app, text="%", command=bagi)
B3.grid(row=2, column=2)

B4 = Button(my_app, text="x", command=kali)
B4.grid(row=2, column=3)

my_app.mainloop()
