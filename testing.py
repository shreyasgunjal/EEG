from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    from tkinter import ttk
   
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    from PIL import Image, ImageTk

    root = tk.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.configure(background="pink")
    
    # image2 = Image.open('img1.jpg')
    # image2 = image2.resize((700, 700), Image.ANTIALIAS)

    # background_image = ImageTk.PhotoImage(image2)

    # background_label = tk.Label(root, image=background_image)

    # background_label.image = background_image

    # background_label.place(x=0, y=0)
    
    lag1_mean_0 = tk.StringVar()
    lag1_mean_1 = tk.StringVar()
    lag1_mean_q1_0 = tk.StringVar()
    lag1_logcovM_0_0 = tk.StringVar()
    lag1_logcovM_0_1 = tk.StringVar()
    lag1_logcovM_0_2 = tk.StringVar()
    lag1_logcovM_0_3 = tk.StringVar()
    lag1_logcovM_1_1 = tk.StringVar()
    lag1_freq_020_0 = tk.StringVar()
    lag1_freq_030_0 = tk.StringVar()
    lag1_freq_041_0 = tk.StringVar()
    lag1_freq_051_0 = tk.StringVar()
    lag1_freq_061_0 = tk.StringVar()
    lag1_freq_071_0 = tk.StringVar()
    freq_740_3 = tk.StringVar()
    freq_750_3 = tk.StringVar()
    
   
    #=============== =====================================================================================================

    def Detect():
        e1=lag1_mean_0.get()
        print(e1)
        
        e2=lag1_mean_1.get()
        print(e2)
        
        e3=lag1_mean_q1_0.get()
        print(e3)
       
        e4=lag1_logcovM_0_0.get()
        print(e4)
        
        e5=lag1_logcovM_0_1.get()
        print(e5)
        
        
        e6=lag1_logcovM_0_2.get()
        print(e6)
        
        e7=lag1_logcovM_0_3.get()
        print(e7)
        
        e8=lag1_logcovM_1_1.get()
        print(e8)
        
        
        e9=lag1_freq_020_0.get()
        print(e9)
       
        e10=lag1_freq_030_0.get()
        print(e10)
        
        e11=lag1_freq_041_0.get()
        print(e11)
       
        e12=lag1_freq_051_0.get()
        print(e12)
        
        e13=lag1_freq_061_0.get()
        print(e13)
        
        e14=lag1_freq_071_0.get()
        print(e14)
        
        e15=freq_740_3.get()
        print(e15)
        
        e16=freq_750_3.get()
        print(e16)
        
        
       
        
        
        #########################################################################################
        
        from joblib import dump , load
        
        a1=load(r'E:/EEG_signal 100% Code/model.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16]])
        print(v)
       
        # print("V[0]"+v[0])
        if v[0]==0:
            print("0")
            yes = tk.Label(root,text="Normal detected",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=650,y=100)
           
                   
        elif v[0]==1:
            print("1")
            no = tk.Label(root, text="Medium Stress Detected", background="red", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=650, y=100)
        
        elif v[0]==2:
            print("2")
            no = tk.Label(root, text="High Stress Detected", background="red", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=650, y=100)
            
        



    l1=tk.Label(root,text="lag1_mean_0",background="purple",font=('times', 15, ' bold '),width=22)
    l1.place(x=200,y=50)
    lag1_mean_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_mean_0)
    lag1_mean_0.place(x=500,y=50)

    l2=tk.Label(root,text="lag1_mean_1",background="purple",font=('times', 15, ' bold '),width=22)
    l2.place(x=200,y=100)
    lag1_mean_1=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_mean_1)
    lag1_mean_1.place(x=500,y=100)
    
    

    l3=tk.Label(root,text="lag1_mean_q1_0",background="purple",font=('times', 15, ' bold '),width=22)
    l3.place(x=200,y=150)
    lag1_mean_q1_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_mean_q1_0)
    lag1_mean_q1_0.place(x=500,y=150)
    

    l4=tk.Label(root,text="lag1_logcovM_0_0",background="purple",font=('times', 15, ' bold '),width=22)
    l4.place(x=200,y=200)
    lag1_logcovM_0_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_logcovM_0_0)
    lag1_logcovM_0_0.place(x=500,y=200)
    
   

    l5=tk.Label(root,text="lag1_logcovM_0_1",background="purple",font=('times', 15, ' bold '),width=22)
    l5.place(x=200,y=250)
    lag1_logcovM_0_1=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_logcovM_0_1)
    lag1_logcovM_0_1.place(x=500,y=250)
    
   

    l6=tk.Label(root,text="lag1_logcovM_0_2",background="purple",font=('times', 15, ' bold '),width=22)
    l6.place(x=200,y=300)
    lag1_logcovM_0_2=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15), textvar = lag1_logcovM_0_2)
    lag1_logcovM_0_2.place(x=500,y=300)
    
    
    l7=tk.Label(root,text="lag1_logcovM_0_3",background="purple",font=('times', 15, ' bold '),width=22)
    l7.place(x=200,y=350)
    lag1_logcovM_0_3=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_logcovM_0_3)
    lag1_logcovM_0_3.place(x=500,y=350)
    
    

    l8=tk.Label(root,text="lag1_logcovM_1_1",background="purple",font=('times', 15, ' bold '),width=22)
    l8.place(x=200,y=400)
    lag1_logcovM_1_1=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_logcovM_1_1)
    lag1_logcovM_1_1.place(x=500,y=400)

    l9=tk.Label(root,text="lag1_freq_020_0",background="purple",font=('times', 15, ' bold '),width=22)
    l9.place(x=200,y=450)
    lag1_freq_020_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_freq_020_0)
    lag1_freq_020_0.place(x=500,y=450)

    l10=tk.Label(root,text="lag1_freq_030_0",background="purple",font=('times', 15, ' bold '),width=22)
    l10.place(x=200,y=500)
    lag1_freq_030_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_freq_030_0)
    lag1_freq_030_0.place(x=500,y=500)

    l11=tk.Label(root,text="lag1_freq_041_0",background="purple",font=('times', 15, ' bold '),width=22)
    l11.place(x=200,y=550)
    lag1_freq_041_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_freq_041_0)
    lag1_freq_041_0.place(x=500,y=550)

    l12=tk.Label(root,text="lag1_freq_051_0",background="purple",font=('times', 15, ' bold '),width=22)
    l12.place(x=200,y=600)
    lag1_freq_051_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_freq_051_0)
    lag1_freq_051_0.place(x=500,y=600)

    l13=tk.Label(root,text="lag1_freq_061_0",background="purple",font=('times', 15, ' bold '),width=22)
    l13.place(x=200,y=650)
    lag1_freq_061_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_freq_061_0)
    lag1_freq_061_0.place(x=500,y=650)
    
    l14=tk.Label(root,text="lag1_freq_071_0",background="purple",font=('times', 15, ' bold '),width=22)
    l14.place(x=900,y=50)
    lag1_freq_071_0=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=lag1_freq_071_0)
    lag1_freq_071_0.place(x=1200,y=50)

    l15=tk.Label(root,text="freq_740_3",background="purple",font=('times', 15, ' bold '),width=22)
    l15.place(x=900,y=100)
    freq_740_3=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=freq_740_3)
    freq_740_3.place(x=1200,y=100)

    l16=tk.Label(root,text="freq_750_3",background="purple",font=('times', 15, ' bold '),width=22)
    l16.place(x=900,y=150)
    freq_750_3=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 15),textvar=freq_750_3)
    freq_750_3.place(x=1200,y=150)
   

   
    
   

    
    
    

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=700,y=400)



    root.mainloop()

Train()