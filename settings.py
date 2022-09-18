from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
#import cv2
#import os
#import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
#import pyttsx3

#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

#def speak_va(transcribed_query):
    #engine.say(transcribed_query)
    #engine.runAndWait()


mydata=[]
class Settings:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")

        #background image
        img3 = Image.open(r"pic\dyci.jpg")
        img3=img3.resize((1530, 790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
       
        
      


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="SYSTEM SETTINGS",font=("times new roman",30,"bold"),bg="dark blue",fg="white")
        title_lbl.place(x=0,y=0,width=1600,height=50)

        # different buttons with images
       
        # department button
        img5 = Image.open(r"pic/department.png")
        img5 = img5.resize((260, 260), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        btn1.place(x=60, y=80, width=195, height=195)

        btn1_1 = Button(bg_img, text="Department Settings", cursor="hand2", font=("times new roman", 13, "bold"),
                         bg="darkblue", fg="white")
        btn1_1.place(x=60, y=245, width=195, height=40)

        # admin
        img6 = Image.open(r"pic/admin.png")
        img6 = img6.resize((260, 260), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        btn1.place(x=600, y=80, width=195, height=195)

        btn1_2 = Button(bg_img, text="Admin", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn1_2.place(x=600, y=245, width=195, height=40)

         # See User
        img7 = Image.open("pic/see_user.png")
        img7 = img7.resize((260, 260), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn3 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        btn3.place(x=880, y=80, width=195, height=195)

        btn3_3 = Button(bg_img, text="See User", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn3_3.place(x=880, y=245, width=195, height=40)


        #course
        img8 = Image.open("pic/student_details_settings.png")
        img8 = img8.resize((260, 260), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        btn4.place(x=330, y=80, width=195, height=195)

        btn4_4 = Button(bg_img, text="Course Settings", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn4_4.place(x=330, y=245, width=195, height=40)

if __name__ == "__main__":
     root=Tk()
     obj=Settings(root)
     root.mainloop()