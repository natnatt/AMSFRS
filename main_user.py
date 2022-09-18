from tkinter import*
from tkinter import ttk
from turtle import right
from PIL import Image, ImageTk
from student import Student
import tkinter
import os
from face_recognition import recognize
from attendace import Attendance

class Face_Recogniton_Systems:
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

        
         # Face Detection button
        img6 = Image.open("image/face_detector.jpg")
        img6 = img6.resize((250, 250), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn2 = Button(bg_img, image=self.photoimg6, cursor="hand2", command = self.face_data)
        btn2.place(x=130, y=200, width=250, height=250)

        btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2",command = self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn2_2.place(x=130, y=410, width=250, height=40)

         # attendance button
        img7 = Image.open("image/attendance.jpg")
        img7 = img7.resize((250, 250), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn3 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.attendance_)
        btn3.place(x=460, y=200, width=250, height=250)

        btn3_3 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn3_3.place(x=460, y=410, width=250, height=40)

         # Developer button
        img11 = Image.open("image/developer.jpg")
        img11 = img11.resize((250, 250), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        btn7 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        btn7.place(x=800, y=200, width=250, height=250)

        btn7_7 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn7_7.place(x=800, y=410, width=250, height=40)

#         # Exit button
        img12 = Image.open("image/exit.jpg")
        img12 = img12.resize((250, 250), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn8 = Button(bg_img, image=self.photoimg12, cursor="hand2",command=self.iexit)
        btn8.place(x=1140, y=200, width=250, height=250)

        btn8_8 = Button(bg_img, text="Exit", cursor="hand2",command = self.iexit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        btn8_8.place(x=1140, y=410, width=250, height=40)



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

   def attendance_(self):
     self.new_window = Toplevel(self.root)
     self.app = Attendance(self.new_window)
   
   def face_data(self):
     self.new_window = Toplevel(self.root)
     self.app = recognize(self.new_window)

  # def (self):
   #  self.new_window = Toplevel(self.root)
    # self.app = Attendance(self.new_window)





        
# ________________________________________________________________function____________________________________________________________________________

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recogniton_Systems(root)
    root.mainloop()



