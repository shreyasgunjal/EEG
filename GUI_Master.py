from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
import time
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import tkinter as tk
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.naive_bayes import GaussianNB

import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
root = tk.Tk()
root.title("EEG Stress detection")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('5.jpeg')

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


lbl = tk.Label(root, text="EEG Stress Level Detection System ", font=('times', 35,' bold '), height=1, width=50,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Model_Training():
    start = time.time()
    data = pd.read_csv("E:/EEG_signal 100% Code/new dataset.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['lag1_mean_0'] = le.fit_transform(data['lag1_mean_0'])
    data['lag1_mean_1'] = le.fit_transform(data['lag1_mean_1'])
    data['lag1_mean_q1_0'] = le.fit_transform(data['lag1_mean_q1_0'])
    data['lag1_logcovM_0_0'] = le.fit_transform(data['lag1_logcovM_0_0'])
    data['lag1_logcovM_0_1'] = le.fit_transform(data['lag1_logcovM_0_1'])
    data['lag1_logcovM_0_2'] = le.fit_transform(data['lag1_logcovM_0_2'])
    data['lag1_logcovM_0_3'] = le.fit_transform(data['lag1_logcovM_0_3'])
    data['lag1_logcovM_1_1'] = le.fit_transform(data['lag1_logcovM_1_1'])
    data['lag1_freq_020_0'] = le.fit_transform(data['lag1_freq_020_0'])
    data['lag1_freq_030_0'] = le.fit_transform(data['lag1_freq_030_0'])
    data['lag1_freq_041_0'] = le.fit_transform(data['lag1_freq_041_0'])
    data['lag1_freq_051_0'] = le.fit_transform(data['lag1_freq_051_0'])
    data['lag1_freq_061_0'] = le.fit_transform(data['lag1_freq_061_0'])
    data['lag1_freq_071_0'] = le.fit_transform(data['lag1_freq_071_0'])
    data['freq_740_3'] = le.fit_transform(data['freq_740_3'])
    data['freq_750_3'] = le.fit_transform(data['freq_750_3'])   

    """Feature Selection => Manual"""
    x = data.drop(['Label'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Label']
    print(type(y))
    x.shape
    
    
    """Feature Selection => Manual"""
    x = data.drop(['prognosis'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['prognosis']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=15)

    

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2,random_state=0)
    #X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    classifier = Sequential()
    classifier.add(Dense(activation = "relu", 
                         units = 8, kernel_initializer = "uniform"))
    classifier.add(Dense(activation = "relu", units = 14, 
                         kernel_initializer = "uniform"))
    classifier.add(Dense(activation = "sigmoid", units = 1, 
                         kernel_initializer = "uniform"))
    classifier.add(Dropout(0.2))
    classifier.compile(optimizer = 'adam' , loss = 'binary_crossentropy', 
                       metrics = ['accuracy'] )
    
    
    classifier.fit(X_train , Y_train , epochs = 200  )
    
    y_pred = classifier.predict(X_test)
    y_pred = (y_pred > 0.5)
    
    #classifier.save( "E:/EEG_signal/EEG.h5")
    
    print("Classification Report :\n")
    repo = (classification_report(Y_test, y_pred))
    print(repo)
    print("\n")
    print("Confusion Matrix :")
    cm = confusion_matrix(Y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix
 
    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Reds)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    accuracy = (cm[0][0]+cm[1][1])/(cm[0][1] + cm[1][0] +cm[0][0] +cm[1][1])
    end = time.time()
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    print(ET)
    print("CNN Accuracy :")
    print(accuracy*100)
    print("\n")
    yes = tk.Label(root,text=accuracy*100,background="green",foreground="white",font=('times', 20, ' bold '),width=15)
    yes.place(x=400,y=400)
    print("Classification Report :\n")
    repo = (classification_report(Y_test, y_pred))
    print(repo)
    print("\n")
    # rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(Y_test,y_pred)
    # sns.set_style('whitegrid')
    # plt.figure(figsize=(10,5))
    # plt.title('Reciver Operating Characterstic Curve')

    # plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='CSNN Classifier',color='red')  
    # plt.plot([0,1],ls='--',color='blue')
    # plt.plot([0,0],[1,0],color='green')
    # plt.plot([1,1],color='green')
    # plt.ylabel('True positive rate')
    # plt.xlabel('False positive rate')
    # plt.legend()
    # plt.show()
    
    from joblib import dump
    dump (classifier,"model.joblib")
    print("Model saved as model.joblib")



def call_file():
    import testing
    testing.Train()


def window():
    root.destroy()

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Model Training", command=Model_Training, width=15, height=2)
# button3.place(x=5, y=170)

button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Detect Stress", command=call_file, width=15, height=2)
button4.place(x=5, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''