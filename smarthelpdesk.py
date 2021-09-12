from tkinter import *
import tkinter as tk
import time
import os
from tkinter import messagebox
import cv2

# ---------------------------- Register Screen Function ------------------
def register():
    global register_screen
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="Gray").pack()
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
    Button(register_screen, text="Register", width=10, height=1, bg="Gray", command=register_user).pack()



def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# ---------------------------- Function Ends here ----------------------

def login():
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    global root
    root = Tk()
    root.geometry("1280x720+0+0")
    root.title("Hospital Management System")
    username_verify = StringVar()
    password_verify = StringVar()
    Tops = Frame(root, bg="white", width=50, height=50, relief=RAISED)
    Tops.pack(side=TOP)
    bg_image = tk.PhotoImage(file="adminmode.png")
    x = tk.Label(image=bg_image)
    x.place(y=0, x=0)
    f1 = Frame(root, relief=FLAT)
    f1.pack(expand=YES)
    global localtime
    # ------------------TIME--------------
    localtime = time.asctime(time.localtime(time.time()))
    # ---------------------------------------------------------------------------------------/
    # ----------- top info ------------------------------------------------------------------/

    lblname = Label(f1, font=('aria', 16, 'bold'), text="    Your Name.", fg="brown", bd=20, anchor='w')
    lblname.grid(row=0, column=5)
    username_login_entry = Entry(f1, font=('ariel', 16, 'bold'), textvariable=username_verify, bd=6, insertwidth=6, bg="Gray",
                    justify='left')
    username_login_entry.grid(row=0, column=6)

    lblpassword = Label(f1, font=('aria', 16, 'bold'), text="    Password.", fg="brown", bd=20, anchor='w')
    lblpassword.grid(row=1, column=5)
    password_login_entry = Entry(f1, font=('ariel', 16, 'bold'), textvariable=password_verify, bd=6, insertwidth=6, bg="Gray",
                        justify='left', show='*')
    password_login_entry.grid(row=1, column=6)

    lblTotal = Label(f1, text="-------------------------------", fg="white")
    lblTotal.grid(row=7, columnspan=3)

    btnregister = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Register",
                         bg="Light Blue", command=register)
    btnregister.grid(row=8, column=5)
    btnlogin = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="LOGIN",
                      bg="Light Blue", command=login_verify)
    btnlogin.grid(row=8, column=6)
    btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="BACK",
                     bg="red",
                     command=qexit)
    btnexit.grid(row=8, column=8)
    root.mainloop()


def login_verify():
    global loggedin
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    loggedin = StringVar()
    loggedin = username1
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            employ_port()


        else:
            # Label(root, text="password not recognized", fg="red", font=("calibri", 11)).pack()
            password_not_recognised()

    else:
        user_not_found()


def employ_port():
    root.destroy()
    employee_portal_screen()

def employe_portal():
    rootwn.destroy()
    login()

def patient_portal():
    rootwn.destroy()
    patient_portal_screen()


def t_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(root)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(root)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()





def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()



def qexit():
    root.destroy()
    first_screen()

def patient_back():
    patportal.destroy()
    first_screen()

def employee_back():
    empportal.destroy()
    first_screen()


def labslipback():
    labslipg.destroy()
    patient_portal_screen()

def labreporthistory():
    empportal.destroy()
    chklabreporthist()

def employee_portal_screen_back():
    labhist.destroy()
    employee_portal_screen()

def open_save_report_portal():
    labhist.destroy()
    main_save_report()

def slip_result_back():
    checkrsltscreen.destroy()
    patient_portal_screen()


# ---------------------------------------------------------------

# ------------------- Map function ----------
def back_map():
    mapo.destroy()
    patient_portal_screen()

def open_map_from_pat():
    patportal.destroy()
    map_open()

def map_open():
    def mapoeen():
        global mapo
        mapo = Tk()
        mapo.geometry("684x488")
        mapo.title("Hospital Management System")
        mapo.configure(background='white')
        fr1 = tk.Frame(mapo)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="hosmap.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)

        b1 = tk.Button(mapo, font=('arial', 16), command=back_map, text="BACK", fg="black" ,bg="red" )
        b1.place(x=500, y=400)
        mapo.mainloop()

    mapoeen()



# ----------------- Ends here -----------------



# -------------------- Complain register function starts ------------
# ------------------------------------------------------------------

def open_complain():
    patportal.destroy()
    register_complaints_main()

def back_complain():
    register_scr.destroy()
    patient_portal_screen()

def register_complaints_main():

    def register():
        nbr = patnbr.get()
        rep = yourcomplain.get()
        f= open("complains.txt" , "a+")
        f.write("patient phone nbr: {} \ncomplain: {}\n".format(nbr,rep))
        messagebox.showinfo("Operation Successfull!!!", "Your Report Has been Submitted successfully!!")



    def register_screen():
        global register_scr, patnbr , yourcomplain
        register_scr = Tk()
        patnbr = StringVar()
        yourcomplain = StringVar()
        register_scr.geometry("1280x720")
        register_scr.title("Hospital Management System")
        register_scr.configure(background='white')
        fr1 = tk.Frame(register_scr)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="compscreen.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        l1=tk.Label(register_scr , font=('arial' , 16 ) , text="We are Sorry!! We Will try to resolve your issue :", fg="red")
        l1.place(x=400 , y=300)
        l2 = tk.Label(register_scr, font=('arial', 16), text="Enter your phone nbr :")
        l2.place(x=180, y=400)
        e1=tk.Entry(register_scr , font=('arial' , 16 ), textvariable=patnbr, bd=6,  insertwidth=6, bg="Green",justify='left')
        e1.place(x=400, y=400)
        l3 = tk.Label(register_scr, font=('arial', 16), text="Enter your complain :")
        l3.place(x=190, y=450)
        e2 = tk.Entry(register_scr, font=('arial', 16), textvariable=yourcomplain, bd=6, insertwidth=6,
                      bg="Gray", justify='left')
        e2.place(x=400, y=450)
        b1= tk.Button(register_scr , font=('arial' , 16), command=register, text="Submit" ,fg="red" )
        b1.place(x=500,y=500)
        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)
        b6 = tk.Button(image=myimg6, command=back_complain)
        b6.image = myimg6
        b6.place(x=1120, y=600)
        register_scr.mainloop()

    register_screen()


# ------------------------- complain functions ends----------------------



# ---------------------- BLOOD BANK FUNCTIONS -------------------------
# -------------------------- Starts ------------------------------------

# ------------------ Patient Portal Function ---------------
def open_blood_bank_check():
    patportal.destroy()
    blood_bank_add()

def blood_bank_back():
    blood_bank.destroy()
    patient_portal_screen()

def blood_bank_add():

    def blood_bank_check():
        filename = bloodtype.get()
        b = filename
        # filename = StringVar()
        file = "{}.txt".format(filename)
        list_of_files = os.listdir()
        print(filename)
        if file in list_of_files:
            f= open(file ,"r")
            rea = f.read()
            messagebox.showinfo("Congratulation Blood Found!!!","There are {} bottles of {} blood left in blood bank".format(rea,b))
            f.close()
        else:
            messagebox.showinfo("Sorry!!!", "There is no bottles of {} blood left in bloodbank!!".format(b))


    def blood_bank_show():
        global blood_bank,bloodtype
        blood_bank = Tk()
        bloodtype = StringVar()
        blood_bank.geometry("1280x720")
        blood_bank.title("Hospital Management System")
        blood_bank.configure(background='white')
        fr1 = tk.Frame(blood_bank)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="bloodbanksearchscreen.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        l1=tk.Label(blood_bank , font=('arial' , 16 ) , text="Enter blood Name you want :" )
        l1.place(x=100 , y=400)
        e1=tk.Entry(blood_bank , font=('arial' , 16 ), textvariable=bloodtype, bd=6,  insertwidth=6, bg="Gray",justify='left')
        e1.place(x=400, y=400)
        b1= tk.Button(blood_bank , font=('arial' , 16), text="Check" ,fg="red" ,command=blood_bank_check)
        b1.place(x=470,y=450)
        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)
        b6 = tk.Button(image=myimg6, command=blood_bank_back)
        b6.image = myimg6
        b6.place(x=1120, y=600)
        blood_bank.mainloop()

    blood_bank_show()

# ------------------------- End -----------------------------

# ------------------------ Employee Portal -----------------------

def open_blod_bank_employee():
    empportal.destroy()
    blood_bank_employee()

def blod_back():
    blood_bank_employee.destroy()
    employee_portal_screen()


def blood_bank_employee():

    def blood_bank_employee_check():
        blood = bloodtype_employee.get()
        bot   = bottles.get()
        list_of_files = os.listdir()
        b = blood+".txt"
        if b in list_of_files:
            f = open(b ,"r")
            re =f.read()
            f.close()
            f= open(b , 'w')

            f.write(re+bot)
            f.close()
            messagebox.showinfo("Operation Successfull!!!", "Blood Added to the blood bank!!")
        else:
            filename = open(blood+".txt" , 'w+')
            filename.write(bot)
            filename.close()
            messagebox.showinfo("Operation Successfull!!!", "Blood Added to the blood bank!!")


    def blood_bank_employee_show():
        global blood_bank_employee, bloodtype_employee , bottles
        blood_bank_employee = Tk()
        bloodtype_employee = StringVar()
        bottles = StringVar()
        blood_bank_employee.geometry("1280x720")
        blood_bank_employee.title("Hospital Management System")
        blood_bank_employee.configure(background='white')
        fr1 = tk.Frame(blood_bank_employee)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="bloodbanksearchscreen.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        l1=tk.Label(blood_bank_employee , font=('arial' , 16 ) , text="ADD BLOOD TO THE BANK :", fg="red")
        l1.place(x=400 , y=300)
        l2 = tk.Label(blood_bank_employee, font=('arial', 16), text="Enter Blood Type :")
        l2.place(x=200, y=400)
        e1=tk.Entry(blood_bank_employee , font=('arial' , 16 ), textvariable=bloodtype_employee, bd=6,  insertwidth=6, bg="Gray",justify='left')
        e1.place(x=400, y=400)
        l3 = tk.Label(blood_bank_employee, font=('arial', 16), text="Enter No of Bottles :")
        l3.place(x=200, y=450)
        e2 = tk.Entry(blood_bank_employee, font=('arial', 16), textvariable=bottles, bd=6, insertwidth=6,
                      bg="Gray", justify='left')
        e2.place(x=400, y=450)
        b1= tk.Button(blood_bank_employee , font=('arial' , 16), text="ADD" ,fg="red" ,command=blood_bank_employee_check)
        b1.place(x=500,y=500)
        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)
        b6 = tk.Button(image=myimg6, command=blod_back)
        b6.image = myimg6
        b6.place(x=1120, y=600)
        blood_bank_employee.mainloop()

    blood_bank_employee_show()

# ----------------- ends --------------




# -------------------- Blood Functions End here ---------------------
# -------------------------------------------------------------------


def check_lab_result():
    patportal.destroy()
    main_result_serach()

def main_result_serach():
    def clearallresult():
        checkrsltscreen.destroy()
        entering_id_portal()

    def showlabresult():
        global filename3
        # filename = StringVar()
        filename3 = enter_id.get()
        file1 = filename3 + ".txt"
        # print(filename)
        list_of_files = os.listdir("C:\\Users\\hp\\Desktop\\Hospital Management system GUI TKINTER")
        if file1 in list_of_files:
            f = open(filename3 + ".txt", "r")
            x = 330
            y = 170
            for line in f:
                l = tk.Message(checkrsltscreen, anchor="w", padx=2, pady=2, bd=4, fg="black",
                               font=('ariel', 12),
                                justify="right", text=line, relief="flat", width=100)
                l.place(x=x + 100, y=y + 100, )
                # x +=100
                y += 60
            f.close()
        else:
            messagebox.showinfo("Please Wait!!!", "Result is not uploaded yet!!")

    def entering_id_portal():
        global checkrsltscreen
        global enter_id

        checkrsltscreen = Tk()
        enter_id = StringVar()
        checkrsltscreen.geometry("1280x720")
        checkrsltscreen.title("Hospital Management System")
        checkrsltscreen.configure(background='white')
        fr1 = tk.Frame(checkrsltscreen)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="checklabresultscreen.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        e = tk.Entry(checkrsltscreen, font=('ariel', 16, 'bold'), bd=6, textvariable=enter_id, insertwidth=6,
                     bg="Gray", justify='left')
        e.place(x=400, y=205)
        e1 = tk.Button(checkrsltscreen, padx=8, pady=8, bd=6, fg="black", font=('ariel', 8, 'bold'), width=6,
                       text="Check", command=showlabresult, bg="red")
        e1.place(x=680, y=205)
        e2 = tk.Button(checkrsltscreen, padx=8, pady=8, bd=6, fg="black", font=('ariel', 8, 'bold'), width=6,
                       text="Clear All", command=clearallresult, bg="red")
        e2.place(x=770, y=205)
        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)
        b6 = tk.Button(image=myimg6, command=slip_result_back)
        b6.image = myimg6
        b6.place(x=1120, y=600)
        checkrsltscreen.mainloop()

    entering_id_portal()

def chklabreporthist():

    global labhist
    labhist = Tk()
    labhist.geometry("1280x720")
    labhist.title("Hospital Management System")
    labhist.configure(background='white')
    fr1 = tk.Frame(labhist)
    fr1.pack(side="top")

    bg_image = tk.PhotoImage(file="labreporthistory.png")
    x = tk.Label(image=bg_image)
    x.place(y=0, x=0)
    frec = open("labtest", "r")
    x = -45
    y = 150
    for line in frec:
        l = tk.Message(labhist, anchor="w", justify="right", text=line, relief="raised", width=2000)
        l.place(x=x + 100, y=y + 100, )
        # x +=100
        y += 40
    frec.close()
    up = tk.PhotoImage(file="uploadreportbutton.png")
    upl = up.subsample(2, 2)
    b7 = tk.Button(image=upl, command=open_save_report_portal)
    b7.image = upl
    b7.place(x=950, y=550)

    img6 = tk.PhotoImage(file="back.gif")
    myimg6 = img6.subsample(2, 2)
    b6 = tk.Button(image=myimg6, command=employee_portal_screen_back)
    b6.image = myimg6
    b6.place(x=980, y=600)

    labhist.mainloop()



def save_to_mainback():
    uploadslipg.destroy()
    chklabreporthist()


def main_save_report():

    def clearlabgenrate_slip():
        uploadslipg.destroy()
        labgenrateslip()

    def save_report_to_file():
        labidofpat = lab_id.get()
        nameofpat = name.get()
        ageofpat = age.get()
        genofpat = gender.get()
        ty_of_lab = test_type.get()
        resofpat = resultofreport.get()
        filename = open("{}.txt".format(labidofpat), "w")
        filename.write("Lab id : {}".format(labidofpat))
        filename.write("\nYour Name : " + nameofpat)
        filename.write("\nYour age : " + ageofpat)
        filename.write("\nYour Gender : " + genofpat)
        filename.write("\nTest Type : " + ty_of_lab)
        filename.write("\nResult : " + resofpat)
        filename.close()
        messagebox.showinfo("Operation Successfull!!", "Report Saved Successfully Successfully!!")

    def labgenrateslip():
        global gender, test_type
        global name, lab_id
        global age, resultofreport
        global uploadslipg
        uploadslipg = Tk()
        age = StringVar()
        name = StringVar()
        gender = StringVar()
        test_type = StringVar()
        lab_id = StringVar()
        resultofreport = StringVar()
        uploadslipg.geometry("1280x720")
        uploadslipg.title("Hospital Management System")
        uploadslipg.configure(background='white')
        fr1 = tk.Frame(uploadslipg)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="enteringlabdata.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)

        l0 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Lab ID.", fg="brown", bd=6, anchor='w')
        l0.place(x=200, y=300)
        e0 = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=lab_id, insertwidth=6, bg="Gray",
                      justify='left')
        e0.place(x=330, y=300)
        l1 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Name.", fg="brown", bd=6, anchor='w')
        l1.place(x=200, y=370)
        e1 = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=name, insertwidth=6, bg="Gray",
                      justify='left')
        e1.place(x=330, y=370)
        l2 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Age.", fg="brown", bd=6, anchor='w')
        l2.place(x=200, y=430)
        e2 = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=age, insertwidth=6, bg="Gray",
                      justify='left')
        e2.place(x=330, y=430)
        l3 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Gender.", fg="brown", bd=6, anchor='w')
        l3.place(x=200, y=490)
        e3 = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=gender, insertwidth=6, bg="Gray",
                      justify='left')
        e3.place(x=330, y=490)
        l7 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Test Type", fg="brown", bd=6, anchor='w')
        l7.place(x=200, y=550)
        e7 = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=test_type, insertwidth=6, bg="Gray",
                      justify='left')
        e7.place(x=330, y=550)
        l = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Result.", fg="brown", bd=6, anchor='w')
        l.place(x=200, y=610)
        e = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=resultofreport, insertwidth=6,
                     bg="Gray",
                     justify='left')
        e.place(x=330, y=610)

        e4 = tk.Button(uploadslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
                       text="SAVE REPORT",
                       bg="red", command=save_report_to_file)
        e4.place(x=650, y=350)
        e5 = tk.Button(uploadslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10,
                       text="Clear All",
                       bg="red", command=clearlabgenrate_slip)
        e5.place(x=650, y=450)

        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)

        b6 = tk.Button(image=myimg6, command=save_to_mainback)
        b6.image = myimg6
        b6.place(x=1120, y=600)
        uploadslipg.mainloop()

    labgenrateslip()

#-------------------------------- Patient view data start ------------
#---------------------------------------------------------------------

def patient_data_view_back():
    patientscreen.destroy()
    employee_portal_screen()

def patient_data_view_open():
    empportal.destroy()
    main_patient_data_view()


def main_patient_data_view():
    global patientscreen
    patientscreen = Tk()
    enter_id = StringVar()
    patientscreen.geometry("1280x720")
    patientscreen.title("Hospital Management System")
    patientscreen.configure(background='white')
    fr1 = tk.Frame(patientscreen)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file="patientdatascreen.png")
    x = tk.Label(image=bg_image)
    x.place(y=0, x=0)
    f = open("patientrecord", "r")
    x = 50
    y = 230
    for line in f:
        l = tk.Message(patientscreen, anchor="w", fg="white", font=('ariel', 8, 'bold'),
                       bg="blue", justify="right", text=line, relief="raised", width=2000)
        l.place(x=x + 100, y=y + 20, )
        # x +=100
        y += 30
    f.close()

    img6 = tk.PhotoImage(file="back.gif")
    myimg6 = img6.subsample(2, 2)
    b6 = tk.Button(image=myimg6, command=patient_data_view_back)
    b6.image = myimg6
    b6.place(x=1100, y=600)

    patientscreen.mainloop()

#-------------------------patient view data end --------------------
#-------------------------------------------------------------------

def labslip():
    patportal.destroy()
    def labclear():
        labslipg.destroy()
        labgenrateslip()
    def ok():
        labslipshow.destroy()
        labgenrateslip()
    def labreportnbr():
        global counter
        counter = str
        filename3= open("labid.txt" ,"r")
        counter =int(filename3.read())
        counter +=1
        filename3.close()
        f1 = open("labid.txt", 'w')
        f1.write(str(counter))
        f1.close()

    def slipshow():
        labslipg.destroy()
        labreportnbr()
        labprint()
        global labslipshow
        labslipshow = Tk()
        labslipshow.geometry("800x720")
        labslipshow.title("Hospital Management System")
        labslipshow.configure(background='white')
        fr1 = tk.Frame(labslipshow)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="labreportslip.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        nam = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Your Name: "+na, fg="brown", bd=6, anchor='w')
        nam.place(x=70, y=210)
        agee = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Your Age: "+ag, fg="brown", bd=6, anchor='w')
        agee.place(x=400, y=210)
        gend = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Your Gender: "+mal, fg="brown", bd=6, anchor='w')
        gend.place(x=70, y=260)
        tes =tk.Label(labslipshow,font=('aria', 16, 'bold'), text="Test Type: "+testtype, fg="brown", bd=6, anchor='w')
        tes.place(x=70, y=320)
        labid = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Lab id: {}".format(counter) , fg="brown", bd=6, anchor='w')
        labid.place(x=430, y=320)
        oky = tk.Button(labslipshow, padx=8, pady=4, bd=6, fg="black", font=('ariel', 10, 'bold'), width=10, text="OK",
                       bg="red", command=ok )
        oky.place(x=600, y=620)
        labslipshow.mainloop()

    def labprint():
        localtime = time.asctime(time.localtime(time.time()))
        global na,ag,mal
        na = name.get()
        ag = age.get()
        mal = gender.get()
        record =open("labtest", "a+")
        record.write("\n{}      {}  ".format(counter,localtime)+"           " +na+"            "+ag+"         "+mal+"           "+testtype)

        record.close()

    def labgenrateslip():
        global gender,e1,e2,e3
        global testtype
        global name
        global age
        global labslipg
        labslipg = Tk()
        age = StringVar()
        name = StringVar()
        gender = StringVar()
        testtype = StringVar()
        # labslipg = tk.Tk()
        labslipg.geometry("1280x720")
        labslipg.title("Hospital Management System")
        labslipg.configure(background='white')
        fr1 = tk.Frame(labslipg)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="labmain.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        l1 = tk.Label(labslipg, font=('aria', 16, 'bold'), text="Your Name.", fg="brown", bd=6, anchor='w')
        l1.place(x=350, y=370)
        e1 = tk.Entry(labslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=name , insertwidth=6, bg="Gray", justify='left')
        e1.place(x=500, y=370)
        l2 = tk.Label(labslipg, font=('aria', 16, 'bold'), text="Your age.", fg="brown", bd=6, anchor='w')
        l2.place(x=350, y=430)
        e2 = tk.Entry(labslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=age , insertwidth=6, bg="Gray", justify='left')
        e2.place(x=500, y=430)
        l3 = tk.Label(labslipg, font=('aria', 16, 'bold'), text="Gender.", fg="brown", bd=6, anchor='w')
        l3.place(x=350, y=490)
        e3 = tk.Entry(labslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=gender , insertwidth=6, bg="Gray", justify='left')
        e3.place(x=500, y=490)
        e4=tk.Button(labslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Generate Slip",
                             bg="red" ,command= slipshow)
        e4.place(x=400, y=550)
        e5=tk.Button(labslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Clear All",
                             bg="red", command=labclear)
        e5.place(x=600, y=550)
        tkvar = StringVar()

        # Dictionary with options
        choices = {'Comprehensive Metabolic Panel', 'Complete Blood Count', 'Prothrombin Time', 'Basic Metabolic Panel',
                   'URINE TEST', 'Liver Panel', 'Thyroid Stimulating Hormone', 'Hemoglobin A1C', 'HBV','ALT'}
        tkvar.set('Select Test')  # set the default option

        popupMenu = OptionMenu(labslipg, tkvar, *choices )
        Label(labslipg, padx=16, bd=6, fg="black", font=('ariel', 16, 'bold'), width=12,bg="red" , text="Choose Test Type").place(x=800,y=365)
        popupMenu.place(x=800, y=410)
        # on change dropdown value
        def change_dropdown(*args):
             global testtype
             # tkvar.get()
             testtype = tkvar.get()
             # chk()
             # print(tkvar.get())
        # link function to change dropdown
        tkvar.trace('w', change_dropdown)
        def chk():
            print(testtype)


        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)

        b6 = tk.Button(image=myimg6, command=labslipback)
        b6.image = myimg6
        b6.place(x=1120, y=600)
        labslipg.mainloop()
    labgenrateslip()

def slipback():
    slipg.destroy()
    patient_portal_screen()


def mainslip():
    patportal.destroy()
    def clear():
        slipg.destroy()
        genrateslip()
    def ok():
        slips.destroy()
        genrateslip()

    def slipshow():
        slipg.destroy()
        print()
        global slips
        slips = Tk()
        slips.geometry("800x720")
        slips.title("Hospital Management System")
        slips.configure(background='white')
        fr1 = tk.Frame(slips)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="slip_show.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        nam = tk.Label(slips, font=('aria', 16, 'bold'), text="Your Name: "+na, fg="brown", bd=6, anchor='w')
        nam.place(x=70, y=210)
        agee = tk.Label(slips, font=('aria', 16, 'bold'), text="Your Age: "+ag, fg="brown", bd=6, anchor='w')
        agee.place(x=400, y=210)
        gend = tk.Label(slips, font=('aria', 16, 'bold'), text="Your Gender: "+mal, fg="brown", bd=6, anchor='w')
        gend.place(x=70, y=260)
        oky = tk.Button(slips, padx=8, pady=4, bd=6, fg="black", font=('ariel', 10, 'bold'), width=10, text="OK",
                       bg="red", command=ok )
        oky.place(x=600, y=620)
        slips.mainloop()

    def print():
        global localtime
        locatime = time.asctime(time.localtime(time.time()))
        global na,ag,mal
        na = name.get()
        ag = age.get()
        mal = gender.get()
        record =open("patientrecord", "a+")
        record.write(str(locatime+"              " +na+"            "+ag+"         "+mal))
        record.write("\n")
        record.close()

    def genrateslip():
        global gender,e1,e2,e3
        global name
        global age
        global slipg
        slipg = Tk()
        age = StringVar()
        name = StringVar()
        gender = StringVar()
        # slipg = tk.Tk()
        slipg.geometry("1280x720")
        slipg.title("Hospital Management System")
        slipg.configure(background='white')
        fr1 = tk.Frame(slipg)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="slipgen-01.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        l1 = tk.Label(slipg, font=('aria', 16, 'bold'), text="Your Name.", fg="brown", bd=6, anchor='w')
        l1.place(x=350, y=370)
        e1 = tk.Entry(slipg,font=('ariel', 16, 'bold') , bd=6, textvariable=name , insertwidth=6, bg="Gray", justify='left')
        e1.place(x=500, y=370)
        l2 = tk.Label(slipg, font=('aria', 16, 'bold'), text="Your age.", fg="brown", bd=6, anchor='w')
        l2.place(x=350, y=430)
        e2 = tk.Entry(slipg,font=('ariel', 16, 'bold') , bd=6, textvariable=age , insertwidth=6, bg="Gray", justify='left')
        e2.place(x=500, y=430)
        l3 = tk.Label(slipg, font=('aria', 16, 'bold'), text="Gender.", fg="brown", bd=6, anchor='w')
        l3.place(x=350, y=490)
        e3 = tk.Entry(slipg,font=('ariel', 16, 'bold') , bd=6, textvariable=gender , insertwidth=6, bg="Gray", justify='left')
        e3.place(x=500, y=490)
        e4=tk.Button(slipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Generate Slip",
                             bg="red" ,command= slipshow)
        e4.place(x=400, y=550)
        e5=tk.Button(slipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Clear All",
                             bg="red", command=clear)
        e5.place(x=600, y=550)
        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)

        b6 = tk.Button(image=myimg6, command=slipback)
        b6.image = myimg6
        b6.place(x=1120, y=600)
        slipg.mainloop()
    genrateslip()




# -----------------------------------------------



def patient_portal_screen():
    global patportal
    patportal = tk.Tk()
    patportal.geometry("1280x720")
    patportal.title("Hospital Management System")
    patportal.configure(background='white')
    fr1 = tk.Frame(patportal)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file="patientscreen-01.png")
    x = tk.Label(image=bg_image)
    x.place(y=0, x=0)

    imgc1 = tk.PhotoImage(file="slipbutton.png")
    imglo = tk.PhotoImage(file="labexports.png")
    imgc2 = tk.PhotoImage(file="blodbankb.png")
    imgc3 = tk.PhotoImage(file="map.png")
    imgc4 = tk.PhotoImage(file="complaints.png")
    imgchk = tk.PhotoImage(file="checklabresult.png")
    imgc = imgc1.subsample(2, 2)
    imglog = imglo.subsample(2, 2)
    img2 = imgc2.subsample(2, 2)
    img3 = imgc3.subsample(2, 2)
    img4 = imgc4.subsample(2, 2)
    img5 = imgchk.subsample(2, 2)
    b1 = tk.Button(image=imgc, command=mainslip)
    b1.image = imgc
    b2 = tk.Button(image=imglog, command=labslip)
    b2.image = imglog
    b3 = tk.Button(image=img2, command=open_blood_bank_check)
    b3.image = img2
    b4 = tk.Button(image=img3, command=open_map_from_pat)
    b4.image = img3
    b5 = tk.Button(image=img4, command=open_complain)
    b5.image = img4
    b7 = tk.Button(image=img5, command=check_lab_result)
    b7.image = img4
    img6 = tk.PhotoImage(file="back.gif")
    myimg6 = img6.subsample(2, 2)

    b6 = tk.Button(image=myimg6, command=patient_back)
    b6.image = myimg6
    b1.place(x=200, y=500)
    b2.place(x=600, y=500)
    b3.place(x=400, y=300)
    b4.place(x=600, y=400)
    b5.place(x=200, y=400)
    b7.place(x=400, y=600)
    b6.place(x=1120, y=600)

    patportal.mainloop()

def employee_portal_screen():
    # root.destroy()
    global  empportal
    empportal = tk.Tk()
    empportal.geometry("1280x720")
    empportal.title("Hospital Management System")
    empportal.configure(background='white')
    fr1 = tk.Frame(empportal)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file="employescreenuser.png")
    x = tk.Label(image=bg_image)
    x.place(y=0, x=0)
    l1 = tk.Label(empportal, font=('aria', 16, 'bold'), text="Logged in as: "+loggedin, fg="brown", bd=6, anchor='w')
    l1.place(x=1050, y=390)
    imgc1 = tk.PhotoImage(file="blodbankb.png")
    imgc2 = tk.PhotoImage(file="uploadreports.png")
    imgc3 = tk.PhotoImage(file="data.png")
    imgc = imgc1.subsample(2, 2)
    img2 = imgc2.subsample(2, 2)
    imgcl3 = imgc3.subsample(2, 2)
    b1 = tk.Button(image=imgc, command=open_blod_bank_employee)
    b1.image = imgc
    b2 = tk.Button(image=img2, command=labreporthistory)
    b2.image = img2
    b3 = tk.Button(image=imgcl3, command=patient_data_view_open)
    b3.image = imgcl3
    img6 = tk.PhotoImage(file="logout.gif")
    myimg6 = img6.subsample(2, 2)

    b6 = tk.Button(image=myimg6, command=employee_back)
    b6.image = myimg6
    b1.place(x=200, y=400)
    b2.place(x=200, y=300)
    b3.place(x=600, y=300)
    b6.place(x=1120, y=430)
    empportal.mainloop()


def first_screen():
    global rootwn
    rootwn = tk.Tk()
    rootwn.geometry("1280x720")
    rootwn.title("Hospital Management System")
    rootwn.configure(background='white')
    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file="mainscreen-01.png")
    x = tk.Label(image=bg_image)
    x.place(y=0, x=0)
    imgc1 = tk.PhotoImage(file="patientportal.png")
    imglo = tk.PhotoImage(file="employee portal.png")
    imgc = imgc1.subsample(2, 2)
    imglog = imglo.subsample(2, 2)
    b1 = tk.Button(image=imgc, command=patient_portal)
    b1.image = imgc
    b2 = tk.Button(image=imglog, command=employe_portal)
    b2.image = imglog
    img6 = tk.PhotoImage(file="exit.gif")
    myimg6 = img6.subsample(2, 2)
    b6 = tk.Button(image=myimg6, command=rootwn.destroy)
    b6.image = myimg6
    b1.place(x=700, y=423)
    b2.place(x=700, y=353)
    b6.place(x=1161, y=650)
    rootwn.mainloop()






def main_account_screen():
    first_screen()



main_account_screen()