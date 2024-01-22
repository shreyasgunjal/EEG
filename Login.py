import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
#import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('reg1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



#
label_l1 = tk.Label(root, text="___LOG IN___",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="white", width=62, height=2)
label_l1.place(x=0, y=0)

img = Image.open('6.jpg')
img = img.resize((100,70), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=40, y=10)


def registration():
    from subprocess import call
    call(["python","Register.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            # root.destroy()

            from subprocess import call
            call(['python','GUI_Master.py'])
            
            root.destroy()
            
         # ===================================S=============
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')



# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Login Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="#EEEE00", fg="black", width=67, height=3)
# label_l2.place(x=0, y=90)


bg1_icon=ImageTk.PhotoImage(file="m.jpg")

bg_icon=ImageTk.PhotoImage(file="L.jpg")
user_icon=ImageTk.PhotoImage(file="l1.png")
pass_icon=ImageTk.PhotoImage(file="p1.jpg")
        
bg_lbl=tk.Label(root,image=bg1_icon, width=670,height=490)
bg_lbl.place(x=390,y=150)
        
title=tk.Label(root, text="__Login Here__", font=("Times new roman", 30, "bold","italic"),bd=5,bg="white",fg="black")
title.place(x=621,y=175,width=250)
        
Login_frame=tk.Frame(root,bg="white")
Login_frame.place(x=465,y=300)
        
logolbl=tk.Label(Login_frame,image=bg_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username",image=user_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="Green",fg="black")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="red",fg="black")
btn_reg.grid(row=3,column=0,pady=10)
        
        
    
       
        # Login Function



def home():
    from subprocess import call
    call(["python","GUI_Main.py"])
    root.destroy()
    
def window():
  root.destroy()
  
  
def reg():
    from subprocess import call
    call(["python","Register.py"])
    root.destroy()

# def about():
#     from subprocess import call
#     call(["python","aboutus.py"])
#     root.destroy()
    
    
button1 = tk.Button(root, text="HOME", command=home, width=12, height=1,font=('times 15 bold underline'),bd=0, bg="skyblue", fg="white")
button1.place(x=185, y=250)

button2 = tk.Button(root, text="REGISTER",command=reg,width=12, height=1,font=('times 15 bold underline'), bd=0,bg="skyblue", fg="white")
button2.place(x=185, y=350)

button4 = tk.Button(root, text="EXIT", command=window, width=12, height=1,font=('times 15 bold underline'),bd=0,bg="skyblue", fg="white")
button4.place(x=185, y=450)


# button1 = tk.Button(frame_alpr, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="Black", fg="white")
# button1.place(x=150, y=110)

# button2 = tk.Button(frame_alpr, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button2.place(x=150, y=200)

# button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=150, y=300)





root.mainloop()