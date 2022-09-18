from ntpath import join
import string
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
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()



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
        self.root.title("Department")

        self.var_dep=StringVar()
        root.eval('tk::PlaceWindow . center')
       

        #background image
        img3 = Image.open(r"image\background.jpg")
        img3=img3.resize((550, 400),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=550,height=400)

        #lvl
        attendanceId_label=Label(text="Department:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=5,pady=4,sticky=W)

        dep_entry=ttk.Entry(textvariable=self.var_dep,width=20,font=("times new roman",12,"bold"))
        dep_entry.grid(row=2,padx=5,pady=2,sticky=W)

        #rt frame 
        Right_frame=LabelFrame(bd=3,bg="white",relief=RIDGE,text="Department",font=("times new roman",12,"bold"))
        Right_frame.place(x=200,y=2,width=340,height=320)

        table_frame=Frame(Right_frame,bd=3,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=0,width=325,height=290)

        #scroll bar table 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #button
        btn1 = Button(self.root, text="Close", cursor="hand2", font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn1.place(x=80, y=340, width=100, height=30)

        btn2 = Button(self.root, text="Delete", cursor="hand2", font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn2.place(x=230, y=340, width=100, height=30)

        btn3 = Button(self.root, text="Add", cursor="hand2",command=self.add_data, font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn3.place(x=380, y=340, width=100, height=30)

    #==============add=====================

    def add_data(self):
        if self.var_dep.get()=="":
          speak_va("Alert!!! All Fields are Mandatory.")
          messagebox.showerror("Error",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="department")
                my_cursor=conn.cursor()
                my_cursor.execute("CREATE TABLE `department`.value(%s) (`course` VARCHAR(45) NULL);" ,(
                (self.var_dep.get())
                ))

                                             
               
                conn.commit()
                self.fetch_data()
                conn.close()
                speak_va('Student Details has been added successfully.')
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




    #fetch

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="department")
        my_cursor=conn.cursor()
        my_cursor.execute("SHOW TABLES")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                 self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
    
        self.var_dep.set(data[0])



if __name__ == "__main__":
     root=Tk()
     obj=Attendance(root)
     root.mainloop()