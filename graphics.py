from tkinter import*
import tkinter as tk
import time
import os
import random

root = Tk()
root.geometry("1280x720")
root.title("Hospital Management System")


Tops = Frame(root,bg="white",width = 50,height=50,relief=RAISED)
Tops.pack(side=TOP)
bg_image = tk.PhotoImage(file="adminmode.png")
x = tk.Label(image=bg_image)
x.place(y=0, x=0)
f1 = Frame(root,relief=FLAT)
f1.pack(expand=YES)

#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#---------------------------------------------------------------------------------------/
#----------- top info ------------------------------------------------------------------/
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="City Hospital Management System",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text="Hi Welcome to ADMIN PORTAL!!!  Please Enter Login Details",fg="Red",
                bd=10,anchor=W)
lblinfo.grid(row=3,column=0)
global username_verify
global password_verify

username_verify = StringVar()
password_verify = StringVar()

global username_login_entry
global password_login_entry

def login_error():
    lbllogin = Label(f1,font=('ariel' ,16,'bold') ,text="Password or user name incorrect", fg="Red")
    lbllogin.grid(row=6, columnspan=10)

def qexit():
    root.destroy()

def welcomee():
    roo = Tk()
    roo.geometry("800x600+0+0")
    roo.title("Welcome to Employeee Manager")
    roo.mainloop()


def register():
    global register_screen
    register_screen = Tk()
    register_screen.geometry("300x250")
    register_screen.title("Register")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()
    register_screen.mainloop()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open("username_info", "w+")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    txtname.delete(0, END)
    txtpassword.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
             password_not_recognised()

    else:
        user_not_found()


def delete_login_success():
    login_success_screen.destroy()

def loog_exit():
    loog.destroy()
def login_sucess():

    global loog
    loog = Tk()
    loog.geometry("800x600+0+0")
    loog.title("Hospital Management System")
    Label(loog,font=('aria', 20,), text="Choose Option to Enter Respective Portal", bg="light blue",fg="Red",bd=10, anchor=W).pack()
    Label(loog, font=('aria', 20,), text=localtime, fg="steel blue", anchor=W).pack()
    Label(loog, text="\n\n\n").pack()
    emp = Button(loog, text="Employee Portal",padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
               bg="light blue", command=register_user).pack()
    Label(loog, text="").pack()
    emp = Button(loog, text="Patient Portal", padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
                 bg="light blue", command=register_user).pack()
    Label(loog, text="\n\n\n\n").pack()
    # emp = Button(loog, text="EXIT", padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
    #              bg="light blue", command=).pack()
    loog.mainloop()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Tk()
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Tk()
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()
#-----------------------------------------------


lblname = Label(f1, font=( 'aria' ,16, 'bold' ),text="Your Name.",fg="brown",bd=20,anchor='w')
lblname.grid(row=0,column=5)
txtname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=username_verify , bd=6,insertwidth=6,bg="Green" ,justify='left')
txtname.grid(row=0,column=6)

lblpassword = Label(f1, font=( 'aria' ,16, 'bold' ),text="    Password.",fg="brown",bd=20,anchor='w')
lblpassword.grid(row=1,column=5)
txtpassword = Entry(f1,font=('ariel' ,16,'bold'), textvariable=password_verify , bd=6,insertwidth=6,bg="yellow" ,justify='left',show='*' )
txtpassword.grid(row=1,column=6)

lblTotal = Label(f1,text="-------------------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)



btnregister=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Register", bg="Light Blue",command=register)
btnregister.grid(row=8, column=5)
btnlogin=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="LOGIN", bg="Light Blue",command=login_verify)
btnlogin.grid(row=8, column=6)
btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=8, column=8)





root.mainloop()

