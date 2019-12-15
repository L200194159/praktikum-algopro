from tkinter import (Tk, Label, Entry, Button, StringVar)
from tkinter import (LEFT, RIGHT)

my_app = Tk(className="Data Mahasiswa UMS")

L1 = Label(my_app, text="Data Diri Mahasiswa", font=("arial",36))
L1.grid(row=0, column=0, sticky="w")

L2 = Label(my_app, text="Nama", font=("arial",24))
L2.grid(row=1, column=0, sticky="w")

str2 = StringVar(value="Juniar Darma Yati")
E2 = Label(my_app, textvariable=str2, font=("arial",20))
E2.grid(row=1, column=2, sticky="w")

L3 = Label(my_app, text=":", font=("arial",24))
L3.grid(row=1, column=1, sticky="w")

L4 = Label(my_app, text="NIM", font=("arial",24))
L4.grid(row=2, column=0, sticky="w")

str4 = StringVar(value="L200194159")
E4 = Label(my_app, textvariable=str4, font=("arial",20))
E4.grid(row=2, column=2, sticky="w")

L5 = Label(my_app, text=":", font=("arial",24))
L5.grid(row=2, column=1, sticky="w")

L6 = Label(my_app, text="Tempat Lahir", font=("arial",24))
L6.grid(row=3, column=0, sticky="w")

str6 = StringVar(value="Buluh Rampai")
E6 = Label(my_app, textvariable=str6, font=("arial",20))
E6.grid(row=3, column=2, sticky="w")

L7 = Label(my_app, text=":", font=("arial",24))
L7.grid(row=3, column=1, sticky="w")

L8 = Label(my_app, text="Tanggal Lahir", font=("arial",24))
L8.grid(row=4, column=0, sticky="w")

str8 = StringVar(value="14 Juni 2001")
E8 = Label(my_app, textvariable=str8, font=("arial",20))
E8.grid(row=4, column=2, sticky="w")

L9 = Label(my_app, text=":", font=("arial",24))
L9.grid(row=4, column=1, sticky="w")

def close():
    my_app.destroy()

B1 = Button(my_app.quit(), text="close", command=close, font=("arial",24))
B1.grid(row=6, column=0)

my_app.mainloop()
