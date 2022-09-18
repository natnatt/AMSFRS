from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from cv2 import repeat
from tkcalendar import DateEntry
from tkinter import messagebox
import pyttsx3
import mysql.connector
import cv2 
import os
import numpy as np
from time import strftime
from datetime import datetime 

class recognize:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

       

        title_lbl = Label(text="Train Data Set",font=("Britannic Bold", 25, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1550, height=45)  

        #1st image
        img = Image.open("img/FR.png")
        img = img.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1530, height=790)


        btn1 = Button(self.root, text="Face Recognition", cursor="hand2",command=self.face_recog, font=("times new roman", 15, "bold"),
        bg="darkblue", fg="white")
        btn1.place(x=230, y=450, width=250, height=60)


        #==================attendance===========
    def mark_attendance(self,n,r,d):
        with open("oamil.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split(",")
                name_list.append(entry[0])
                print("name content:", name_list)
            if((n not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                #d1 for date variable
                dtString=now.strftime("%H:%M:%S")
                #myDatalist.drop_duplicates(keep=False)
                f.writelines(f"\n{r},{n},{d},{dtString}, {d1},Present")

                







             # face recognition  command=self.face_recog
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)   

            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
                my_cursor=conn.cursor() 

                
                my_cursor.execute("select surname,firstn,midinitial from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n=" ".join(n)

                my_cursor.execute("select student_id from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                print("content",r,n,d)

                if predict < 500:
                # if result[1] < 500:
                    confidence=int((100*(1-predict/300)))
                    # str2 = str(confidence)
                    # confidence = int(100 * (1 - (result[1])/300))
                    # display_string = str(confidence)+'% confidence it is user'
                # cv2.putText(img,display_string(250, 250), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)

                if confidence>75:
                    
                    cv2.putText(img,f"id:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,r,d)
                   
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)   
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            # speak_va("Welcome to Face Recognition World")
            cv2.imshow("Welcome to face Recognition",img)


            if cv2.waitKey(1)==13:
                
                break
        video_cap.release()
        #cv2.destroyAllWindows()








if __name__ == "__main__":
    root=Tk()
    obj=recognize(root)
    root.mainloop() 