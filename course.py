from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
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
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("550x400+0+0")
        self.root.title("Course")

        #background image
        img3 = Image.open(r"image\background.jpg")
        img3=img3.resize((550, 400),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=550,height=400)

        #lvl
        attendanceId_label=Label(text="Department:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=2,pady=4,sticky=W)

        self.atten_status=ttk.Combobox(textvariable=self,font=("times new roman",12,"bold"),state="readonly",width=9)
        self.atten_status["values"]=("Select","CSS","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=0,column=0,padx=100,pady=0,sticky=W)

        attendanceID_entry=ttk.Entry(textvariable=self,width=23,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        #rt frame 
        Right_frame=LabelFrame(bd=3,bg="white",relief=RIDGE,text="Course",font=("times new roman",12,"bold"))
        Right_frame.place(x=200,y=2,width=340,height=320)

        table_frame=Frame(Right_frame,bd=3,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=0,width=325,height=290)

        #scroll bar table 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        #button
        btn1 = Button(self.root, text="Close", cursor="hand2", font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn1.place(x=80, y=340, width=100, height=30)

        btn2 = Button(self.root, text="Delete", cursor="hand2", font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn2.place(x=230, y=340, width=100, height=30)

        btn3 = Button(self.root, text="Add", cursor="hand2", font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn3.place(x=380, y=340, width=100, height=30)

        #================fetch================
    



if __name__ == "__main__":
     root=Tk()
     obj=Attendance(root)
     root.mainloop()