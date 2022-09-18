from tkinter import*
from tkinter import ttk
import tkinter
from turtle import right
from PIL import Image, ImageTk
from student import Student
import tkinter
import os
from tkinter import messagebox
from train import train_data
from face_recognition import recognize
from attendace import Attendance
from settings import Settings

class Face_Recogniton_System:
   def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #1st image
        img = Image.open("image/topbanner.jpg")
        img = img.resize((1550, 130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(y=-5, width=1550, height=130)

        # background image
       
        img4 = Image.open("pic/dyci.jpg")
        img4 = img4.resize((1550, 780), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1550, height=780)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
        font=("Britannic Bold", 25, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1550, height=45)  # using .place u can place things at any part of the window

        # different buttons with images
        # student button
        img5 = Image.open("image/student_details.jpg")
        img5 = img5.resize((250, 250), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        btn1.place(x=130, y=80, width=250, height=250)

        btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        btn1_1.place(x=130, y=290, width=250, height=40)

        
         # Face Detection button
        img6 = Image.open("image/face_detector.jpg")
        img6 = img6.resize((250, 250), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn2 = Button(bg_img, image=self.photoimg6, cursor="hand2", command = self.face_data)
        btn2.place(x=460, y=80, width=250, height=250)

        btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command = self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn2_2.place(x=460, y=290, width=250, height=40)

         # attendance button
        img7 = Image.open("image/attendance.jpg")
        img7 = img7.resize((250, 250), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn3 = Button(bg_img, image=self.photoimg7, cursor="hand2", command = self.attendance_)
        btn3.place(x=800, y=80, width=250, height=250)

        btn3_3 = Button(bg_img, text="Attendance", cursor="hand2",command = self.attendance_, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn3_3.place(x=800, y=290, width=250, height=40)

        # Help Desk button
        #img8 = Image.open("img/scholarImages/helpdesk_ky.png")
        #img8 = img8.resize((250, 250), Image.ANTIALIAS)
        #self.photoimg8 = ImageTk.PhotoImage(img8)

        #btn4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
       # btn4.place(x=1000, y=80, width=250, height=250)

       # btn4_4 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        #btn4_4.place(x=1000, y=245, width=250, height=40)

         # train data button
        img9 = Image.open("image/train_data.jpg")
        img9 = img9.resize((250, 250), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn5 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_dataa)
        btn5.place(x=1140, y=80, width=250, height=250)

        btn5_5 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_dataa, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn5_5.place(x=1140, y=290, width=250, height=40)

#         # Photos button
        img10 = Image.open("image/picture.jpg")
        img10 = img10.resize((250, 250), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn6 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
        btn6.place(x=130, y=365, width=250, height=250)

        btn6_6 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn6_6.place(x=130, y=575, width=250, height=40)

        # settings
        img13 = Image.open("image/settings.png")
        img13 = img13.resize((250, 250), Image.ANTIALIAS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        btn8 = Button(bg_img, image=self.photoimg13, cursor="hand2", command=self.ssettings)
        btn8.place(x=460, y=365, width=250, height=250)

        btn8_8 = Button(bg_img, text="Settings", cursor="hand2",command=self.ssettings, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn8_8.place(x=460, y=575, width=250, height=40)

         # Developer button
        img11 = Image.open("image/developer.jpg")
        img11 = img11.resize((250, 250), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn7 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        btn7.place(x=800, y=365, width=250, height=250)

        btn7_7 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn7_7.place(x=800, y=575, width=250, height=40)

#         # Exit button
        img12 = Image.open("image/exit.jpg")
        img12 = img12.resize((250, 250), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn8 = Button(bg_img, image=self.photoimg12, cursor="hand2",command=self.iexit)
        btn8.place(x=1140, y=365, width=250, height=250)

        btn8_8 = Button(bg_img, text="Exit", cursor="hand2",command=self.iexit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn8_8.place(x=1140, y=575, width=250, height=40)



   def open_img(self):
       os.startfile("data")

 # .................exit button
   def iexit(self):
        #speak_va("Are you sure you want to exit this project?")
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?",parent=self.root)
        if self.iexit>0:
           self.root.destroy()
        else:
            return  


#==================button function================================
   def student_details(self):
     self.new_window = Toplevel(self.root)
     self.app = Student(self.new_window)

   def train_dataa(self):
     self.new_window = Toplevel(self.root)
     self.app = train_data(self.new_window)
   
   def face_data(self):
     self.new_window = Toplevel(self.root)
     self.app = recognize(self.new_window)

   def attendance_(self):
     self.new_window = Toplevel(self.root)
     self.app = Attendance(self.new_window)

   def ssettings(self):
     self.new_window = Toplevel(self.root)
     self.app = Settings(self.new_window)

   
        
# ________________________________________________________________function____________________________________________________________________________

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recogniton_System(root)
    root.mainloop()



