from tkinter import *
import os
import time

# localtime = time.asctime(time.localtime(time.time()))

def login_sucess():
    global root
    root = Tk()
    root.geometry("1280x720")
    root.title("Hospital Management System")
    bg_image = PhotoImage(file="mainscreen-01.png")
    x = Label(image=bg_image)
    x.place(x=0, y=0, relwidth=1, relheight=1)
    x.image = bg_image
    Tops = Frame(root, bg="white", width=1280, height=720, relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(root, width=1280, height=720, relief=SUNKEN)
    f1.pack(side=LEFT)

    f2 = Frame(root, width=1280, height=720, relief=SUNKEN)
    f2.pack(side=RIGHT)
    global localtime
    # ------------------TIME--------------
    localtime = time.asctime(time.localtime(time.time()))
    # ---------------------------------------------------------------------------------------/
    # ----------- top info ------------------------------------------------------------------/
    # lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="Edhi Hospital Management System", fg="Black", bd=10,
    #              anchor='w')
    # lblinfo.grid(row=0, column=0)
    lblinfo = Label(f2, font=('aria', 20,), text=localtime, fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(Tops, font=('aria', 20,), text="", fg="Red",
                    bd=10, anchor=W)
    lblinfo.grid(row=20, column=0)


    # lblTotal = Label(f1, text="-------------------------------", fg="white")
    # lblTotal.grid(row=7, columnspan=3)

    btnregister = Button(f2, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Patient Portal",
                         bg="Light Blue")
    btnregister.grid(row=12, column=0)
    btnlogin = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Employee Portal",
                      bg="Light Blue")
    btnlogin.grid(row=14, column=0)

    btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT",
                     bg="red",command=qexit)

    btnexit.grid(row=16, column=0)
    root.mainloop()

def qexit():
    root.destroy()


def loog_exit():
    loog.destroy()


def employe_portal():
    h=Tk()
    h.geometry("800x600+0+0")
    h.title("Welcome")
    h.mainloop()


def patient_portal():
    p=Tk()
    p.geometry("800x600+0+0")
    p.title("Welcome")
    p.mainloop()


login_sucess()