import tkinter as tk
from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime
import os


# def main_save_report():
#     def clearlabgenrate_slip():
#         uploadslipg.destroy()
#         labgenrateslip()
#
#     def save_report_to_file():
#         labidofpat = lab_id.get()
#         nameofpat = name.get()
#         ageofpat = age.get()
#         genofpat = gender.get()
#         ty_of_lab = test_type.get()
#         resofpat = resultofreport.get()
#         filename = open("{}.txt".format(labidofpat), "w")
#         filename.write("Lab id : {}".format(labidofpat))
#         filename.write("\nYour Name : "+nameofpat)
#         filename.write("\nYour age : "+ageofpat)
#         filename.write("\nYour Gender : "+genofpat)
#         filename.write("\nTest Type : " + ty_of_lab)
#         filename.write("\nResult : "+resofpat)
#         filename.close()
#         messagebox.showinfo("Operation Successfull!!", "Report Saved Successfully Successfully!!")
#
#     def labgenrateslip():
#         global gender,test_type
#         global name,lab_id
#         global age,resultofreport
#         global uploadslipg
#         uploadslipg = Tk()
#         age = StringVar()
#         name = StringVar()
#         gender = StringVar()
#         test_type = StringVar()
#         lab_id = StringVar()
#         resultofreport = StringVar()
#         uploadslipg.geometry("1280x720")
#         uploadslipg.title("Hospital Management System")
#         uploadslipg.configure(background='orange')
#         fr1 = tk.Frame(uploadslipg)
#         fr1.pack(side="top")
#         bg_image = tk.PhotoImage(file="enteringlabdata.png")
#         x = tk.Label(image=bg_image)
#         x.place(y=0, x=0)
#
#         l0 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Lab ID.", fg="brown", bd=6, anchor='w')
#         l0.place(x=200, y=300)
#         e0 = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=lab_id, insertwidth=6, bg="Green",
#                       justify='left')
#         e0.place(x=330, y=300)
#         l1 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Name.", fg="brown", bd=6, anchor='w')
#         l1.place(x=200, y=370)
#         e1 = tk.Entry(uploadslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=name , insertwidth=6, bg="Green", justify='left')
#         e1.place(x=330, y=370)
#         l2 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Age.", fg="brown", bd=6, anchor='w')
#         l2.place(x=200, y=430)
#         e2 = tk.Entry(uploadslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=age , insertwidth=6, bg="Green", justify='left')
#         e2.place(x=330, y=430)
#         l3 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Gender.", fg="brown", bd=6, anchor='w')
#         l3.place(x=200, y=490)
#         e3 = tk.Entry(uploadslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=gender , insertwidth=6, bg="Green", justify='left')
#         e3.place(x=330, y=490)
#         l7 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Test Type", fg="brown", bd=6, anchor='w')
#         l7.place(x=200, y=550)
#         e7 = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=test_type, insertwidth=6, bg="Green",
#                      justify='left')
#         e7.place(x=330, y=550)
#         l = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Result.", fg="brown", bd=6, anchor='w')
#         l.place(x=200, y=610)
#         e = tk.Entry(uploadslipg, font=('ariel', 16, 'bold'), bd=6, textvariable=resultofreport, insertwidth=6, bg="Green",
#                      justify='left')
#         e.place(x=330, y=610)
#
#         e4=tk.Button(uploadslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="SAVE REPORT",
#                              bg="red" ,command= save_report_to_file)
#         e4.place(x=650, y=350)
#         e5=tk.Button(uploadslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Clear All",
#                              bg="red", command=clearlabgenrate_slip)
#         e5.place(x=650, y=450)
#
#         img6 = tk.PhotoImage(file="back.gif")
#         myimg6 = img6.subsample(2, 2)
#
#         b6 = tk.Button(image=myimg6, command=uploadslipg.destroy)
#         b6.image = myimg6
#         b6.place(x=1120, y=600)
#         uploadslipg.mainloop()
#     labgenrateslip()
def main_result_serach():
    def clearallresult():
        checkrsltscreen.destroy()
        entering_id_portal()

    def showlabresult():
        global filename3
        # filename = StringVar()
        filename3 = enter_id.get()
        file1 = filename3+".txt"
        # print(filename)
        list_of_files = os.listdir("C:\\Users\\hp\\Desktop\\Hospital Management system GUI TKINTER")
        if file1 in list_of_files:
            f= open(filename3+".txt","r")
            x = 330
            y = 170
            for line in f:
                l = tk.Message(checkrsltscreen, anchor="w", padx=8, pady=8, bd=6, fg="white", font=('ariel', 16, 'bold'),
                               bg="red",  justify="right", text=line, relief="raised", width=2000)
                l.place(x=x + 100, y=y + 100, )
                # x +=100
                y += 60
            f.close()
        else:
            messagebox.showinfo("Please Wait!!!", "Result is not uploaded yet!!")



    def entering_id_portal():
        global  checkrsltscreen
        global enter_id

        checkrsltscreen = Tk()
        enter_id = StringVar()
        checkrsltscreen.geometry("1280x720")
        checkrsltscreen.title("Hospital Management System")
        checkrsltscreen.configure(background='orange')
        fr1 = tk.Frame(checkrsltscreen)
        fr1.pack(side="top")
        bg_image = tk.PhotoImage(file="checklabresultscreen.png")
        x = tk.Label(image=bg_image)
        x.place(y=0, x=0)
        e = tk.Entry(checkrsltscreen, font=('ariel', 16, 'bold'), bd=6, textvariable=enter_id, insertwidth=6, bg="Green",justify='left')
        e.place(x=400, y=205)
        e1 = tk.Button(checkrsltscreen, padx=8, pady=8, bd=6, fg="black", font=('ariel', 8, 'bold'), width=6,
        text="Check", command=showlabresult,  bg="red" )
        e1.place(x=680, y=205)
        e2 = tk.Button(checkrsltscreen, padx=8, pady=8, bd=6, fg="black", font=('ariel', 8, 'bold'), width=6,
                       text="Clear All", command=clearallresult, bg="red")
        e2.place(x=770, y=205)
        img6 = tk.PhotoImage(file="back.gif")
        myimg6 = img6.subsample(2, 2)
        b6 = tk.Button(image=myimg6, command=checkrsltscreen.destroy)
        b6.image = myimg6
        b6.place(x=1120, y=600)

        checkrsltscreen.mainloop()

    entering_id_portal()

main_result_serach()

# def labslip():
#     def labclear():
#         uploadslipg.destroy()
#         labgenrateslip()
#     def ok():
#         labslipshow.destroy()
#         labgenrateslip()
#     def labreportnbr():
#         global counter
#         counter = str
#         filename3= open("labid.txt" ,"r")
#         counter =int(filename3.read())
#         counter +=1
#         filename3.close()
#         f1 = open("labid.txt", 'w')
#         f1.write(str(counter))
#         f1.close()
#
#     def slipshow():
#         uploadslipg.destroy()
#         labreportnbr()
#         labprint()
#         global labslipshow
#         labslipshow = Tk()
#         labslipshow.geometry("800x720")
#         labslipshow.title("Hospital Management System")
#         labslipshow.configure(background='orange')
#         fr1 = tk.Frame(labslipshow)
#         fr1.pack(side="top")
#         bg_image = tk.PhotoImage(file="labreportslip.png")
#         x = tk.Label(image=bg_image)
#         x.place(y=0, x=0)
#         nam = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Your Name: "+na, fg="brown", bd=6, anchor='w')
#         nam.place(x=70, y=210)
#         agee = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Your Age: "+ag, fg="brown", bd=6, anchor='w')
#         agee.place(x=400, y=210)
#         gend = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Your Gender: "+mal, fg="brown", bd=6, anchor='w')
#         gend.place(x=70, y=260)
#         tes =tk.Label(labslipshow,font=('aria', 16, 'bold'), text="Test Type: "+testtype, fg="brown", bd=6, anchor='w')
#         tes.place(x=70, y=320)
#         labid = tk.Label(labslipshow, font=('aria', 16, 'bold'), text="Lab id: {}".format(counter) , fg="brown", bd=6, anchor='w')
#         labid.place(x=430, y=320)
#         oky = tk.Button(labslipshow, padx=8, pady=4, bd=6, fg="black", font=('ariel', 10, 'bold'), width=10, text="OK",
#                        bg="red", command=ok )
#         oky.place(x=600, y=620)
#         labslipshow.mainloop()
#
#     def labprint():
#         global na,ag,mal
#         na = name.get()
#         ag = age.get()
#         mal = gender.get()
#         record =open("labtest", "a+")
#         record.write("Labid     DATE & TIME               Patient name            Age         Gender          TEST TYPE\n")
#         record.write(strftime("{}      [%Y-%m-%d] [%H:%M:%S]  ".format(counter), gmtime())+"           " +na+"            "+ag+"         "+mal+"           "+testtype)
#         record.write("\n---------------------------------------------------------------------------")
#         record.write("\n\n")
#         record.close()
#
#     def labgenrateslip():
#         global gender,e1,e2,e3
#         global testtype
#         global name
#         global age
#         global uploadslipg
#         uploadslipg = Tk()
#         age = StringVar()
#         name = StringVar()
#         gender = StringVar()
#         testtype = StringVar()
#         # uploadslipg = tk.Tk()
#         uploadslipg.geometry("1280x720")
#         uploadslipg.title("Hospital Management System")
#         uploadslipg.configure(background='orange')
#         fr1 = tk.Frame(uploadslipg)
#         fr1.pack(side="top")
#         bg_image = tk.PhotoImage(file="labmain.png")
#         x = tk.Label(image=bg_image)
#         x.place(y=0, x=0)
#         l1 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Your Name.", fg="brown", bd=6, anchor='w')
#         l1.place(x=350, y=370)
#         e1 = tk.Entry(uploadslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=name , insertwidth=6, bg="Green", justify='left')
#         e1.place(x=500, y=370)
#         l2 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Your age.", fg="brown", bd=6, anchor='w')
#         l2.place(x=350, y=430)
#         e2 = tk.Entry(uploadslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=age , insertwidth=6, bg="Green", justify='left')
#         e2.place(x=500, y=430)
#         l3 = tk.Label(uploadslipg, font=('aria', 16, 'bold'), text="Gender.", fg="brown", bd=6, anchor='w')
#         l3.place(x=350, y=490)
#         e3 = tk.Entry(uploadslipg,font=('ariel', 16, 'bold') , bd=6, textvariable=gender , insertwidth=6, bg="Green", justify='left')
#         e3.place(x=500, y=490)
#         e4=tk.Button(uploadslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Generate Slip",
#                              bg="red" ,command= slipshow)
#         e4.place(x=400, y=550)
#         e5=tk.Button(uploadslipg, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="Clear All",
#                              bg="red", command=labclear)
#         e5.place(x=600, y=550)
#         tkvar = StringVar()
#
#         # Dictionary with options
#         choices = {'Comprehensive Metabolic Panel', 'Complete Blood Count', 'Prothrombin Time', 'Basic Metabolic Panel',
#                    'URINE TEST', 'Liver Panel', 'Thyroid Stimulating Hormone', 'Hemoglobin A1C', 'HBV','ALT'}
#         tkvar.set('Select Test')  # set the default option
#
#         popupMenu = OptionMenu(uploadslipg, tkvar, *choices )
#         Label(uploadslipg, padx=16, bd=6, fg="black", font=('ariel', 16, 'bold'), width=12,bg="red" , text="Choose Test Type").place(x=800,y=365)
#         popupMenu.place(x=800, y=410)
#         # on change dropdown value
#         def change_dropdown(*args):
#              global testtype
#              # tkvar.get()
#              testtype = tkvar.get()
#              # chk()
#              # print(tkvar.get())
#         # link function to change dropdown
#         tkvar.trace('w', change_dropdown)
#         def chk():
#             print(testtype)
#
#
#         img6 = tk.PhotoImage(file="back.gif")
#         myimg6 = img6.subsample(2, 2)
#
#         b6 = tk.Button(image=myimg6, command=uploadslipg.destroy)
#         b6.image = myimg6
#         b6.place(x=1120, y=600)
#         uploadslipg.mainloop()
#     labgenrateslip()
# #
# #
# labslip()










