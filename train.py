from sqlite3 import connect
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pyttsx3
import mysql.connector
import cv2 
import os
import numpy as np

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class train_data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")

        

       

        title_lbl = Label(text="Train Data Set",font=("Britannic Bold", 25, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1550, height=45)  

        #1st image
        img = Image.open("img/tdd.png")
        img = img.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=1530, height=790)


        btn1 = Button(self.root, text="TRAIN DATA", cursor="hand2",command=self.train_classifier, font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn1.place(x=980, y=450, width=225, height=60)

    def train_classifier(self):
        data_dir=("data")
       
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        print("path",path)
        faces=[]
        ids=[]

     

     #   conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
     #  my_cursor=conn.cursor()
     #   if len(data)!=0:
     #       self.student_table.delete(*self.student_table.get_children())
     #       for i in data:
     #            self.student_table.insert("",END,values=i)
     #       conn.commit()
     #   conn.close()

    
        conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
        my_cursor=conn.cursor()
        my_cursor.execute("select student_id from student")
        data=my_cursor.fetchall()
        
        print("Total number of rows in table: ", my_cursor.rowcount)

        print("\nPrinting each row")

        for row in data:
            print("Id = ", row[0], )

        

        
        for image in path:
            print("qwe",path)
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            print(imageNp)
            id=int(os.path.split(image)[1].split('.')[1])
            print("sad")
            print(id)
            print(image)

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        print("con",ids)

        # Train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        speak_va("Training datasets completed successfully!")
        messagebox.showinfo("Result","Training datasets completed successfully!",parent=self.root)
        self.root.destroy()



if __name__ == "__main__":
    root=Tk()
    obj=train_data(root)
    root.mainloop() 





