from sre_parse import State
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox
import pyttsx3
import mysql.connector
import cv2 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()







class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ##### Variables  #####
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_sname=StringVar()
        self.var_std_first=StringVar()
        self.var_std_mid=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()

        #1st image
        img = Image.open("student_img/topbanner.jpg")
        img = img.resize((1550, 130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=-5, width=1550, height=130)

        
        img4 = Image.open("student_img/background.jpg")
        img4 = img4.resize((1550, 780), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=120, width=1550, height=780)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
        font=("Britannic Bold", 25, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1550, height=45)  

        main_frame=Frame(bg_img,bd=2,bg="white",)
        main_frame.place(x=25,y=50,width=1480,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Algerian",12,"bold"))
        left_frame.place(x=25,y=5,width=700,height=585)

        # img_left=Image.open(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Images\NCIT.jpg")
        # img_left = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Images\re1.jpg")
        img_left = Image.open("img/1234.png")
        img_left = img_left.resize((690,100),Image.ANTIALIAS)  
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0,width=690,height=100)

         #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=100,width=685,height=115)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=18)
        dep_combo["values"]=("Select Department","CCS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
    
        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=18)
        course_combo["values"]=("Select Course","BS Computer Science", "BS Information Technology" ,"BS Computer Engineering")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year Level",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=18)
        year_combo["values"]=("Select Year","1st Year","2nd Year","3rd Year","4th Year","5th Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=18)
        semester_combo["values"]=("Select Semester","Semester-I","Semester-II")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=220,width=685,height=335)

        #studen ID 
        studentId_label=Label(class_student_frame,text="StudentID/LRN:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

     #  validate_id=self.root.register(self.checkid)
     #  studentId_entry.config(validate='key',validatecommand=(validate_id,'%P'))

      #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_sname,width=18,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        studentName_entry=Label(class_student_frame,text="surname",font=("times new roman",6,"bold"),fg="red",bg="white")
        studentName_entry.place(x=475, y=25)
        # call back and validation
        # validate_name=self.root.register(self.checkname)
        # studentName_entry.config(validate='key',validatecommand=(validate_name,'%P'))
        #first name
        studentFn_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_first,width=18,font=("times new roman",13,"bold"))
        studentFn_entry.grid(row=1,column=3,padx=10,sticky=W)
        studentFn_entry=Label(class_student_frame,text="First name",font=("times new roman",6,"bold"),fg="red",bg="white")
        studentFn_entry.place(x=475, y=65)
        #middle name
        studentmid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_mid,width=18,font=("times new roman",13,"bold"))
        studentmid_entry.grid(row=2,column=3,padx=10,sticky=W)
        studentmid_entry=Label(class_student_frame,text="MIddle name",font=("times new roman",6,"bold"),fg="red",bg="white")
        studentmid_entry.place(x=475, y=105)


    #Section
        class_div_label=Label(class_student_frame,text="Section:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_sec,font=("times new roman",13,"bold"),state="readonly",width=16)
        div_combo["values"]=("Select Section","A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Select Gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

         #birth date
        dob_label=Label(class_student_frame,text="Birth Date:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        #dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",13,"bold"))
        #dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        cal = DateEntry(class_student_frame,textvariable=self.var_dob, width=23, year=2019, month=6, day=22, 
         background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=3,column=3,padx=10, pady=10)
      
        # validate_date=self.root.register(self.grad_date)
        # dob_entry.config(validate='key',validatecommand=(validate_date,'%P'))

         #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        email=Label(class_student_frame,text="*ex123@gmail.com",font=("times new roman",6,"bold"),fg="red",bg="white")
        # pswd.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        email.place(x=150, y=149)


        # validate_email=self.root.register(self.checkemail)
        # email_entry.config(validate='key',validatecommand=(validate_email,'%P'))

         #Phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",13,"bold"))
        phone_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #validate_phone=self.root.register(self.checkphone)
        #phone_entry.config(validate='key',validatecommand=(validate_phone,'%P'))

        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #validate_address=self.root.register(self.checkaddress)
        #address_entry.config(validate='key',validatecommand=(validate_address,'%P'))

        def disalbe():
            take_photo_btn['state']='disabled'
        def enable():
            take_photo_btn['state']='normal'

          #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes",command = enable)
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO",command = disalbe)
        radiobtn2.grid(row=5,column=1)

         #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=235,width=660,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="Clear",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)

       #frame for take photo and update photo
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=270,width=660,height=35)

  


        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=33,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",command=self.generate_dataset,width=33,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        update_photo_btn.grid(row=0,column=1)


         
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Algerian",12,"bold"))
        right_frame.place(x=750,y=5,width=700,height=585)

        img_right = Image.open("img/123.png")
        img_right = img_right.resize((690,100),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0,width=690,height=100)

        ##Search System
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=100,width=685,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="white",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=11,textvariable=self.var_search)
        search_combo["values"]=("Select","student_id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=17,textvariable=self.var_searchtxt,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    


        search_btn=Button(search_frame,text="Search",width=10,command=self.search_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="darkblue",fg="white",command=self.show_all)
        showAll_btn.grid(row=0,column=4,padx=4)


       # search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Algerian",12,"bold"))
       # search_frame.place(x=5,y=100,width=685,height=70)

        #search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),Slue",fg="white")
       # search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

       # search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",13,"bold"),state="readonly",width=11)
        #search_combo["values"]=("Select","ID")
       # search_combo.current(0)
       # search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


       # search_entry=ttk.Entry(search_frame,textvariable=self.var_searchtxt,width=17,font=("times new roman",13,"bold"))
       # search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=685,height=375)

        #scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","fname","lname","mname","add","phone","photo","sec","gen","email","birth"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("fname",text="FIrst Name")
        self.student_table.heading("lname",text="Last Name")
        self.student_table.heading("mname",text="Middle Name")
        self.student_table.heading("add",text="Address")
        self.student_table.heading("phone",text="Phonenumber")
        self.student_table.heading("photo",text="Photo sample")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("birth",text="Birthdate")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=170)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("fname",width=100)
        self.student_table.column("lname",width=100)
        self.student_table.column("mname",width=100)
        self.student_table.column("add",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("birth",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_sname.get()=="" or self.var_std_id.get()==""or self.var_radio1.get()=="":
          speak_va("Alert!!! All Fields are Mandatory.")
          messagebox.showerror("Error",'Invalid email Enter valid email like user@gmail.com',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                               self.var_dep.get(),
                                               self.var_course.get(),
                                               self.var_year.get(),
                                               self.var_semester.get(),
                                               self.var_std_id.get(),
                                               self.var_std_first.get(),
                                               self.var_std_sname.get(),
                                               self.var_std_mid.get(),
                                               self.var_address.get(),
                                               self.var_phone.get(),
                                               self.var_radio1.get(),
                                               self.var_sec.get(),
                                               self.var_gender.get(),
                                               self.var_email.get(),
                                               self.var_dob.get()
                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                speak_va('Student Details has been added successfully.')
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
       
        

        #-------------fetch------------

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                 self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        

    #----------get cursor-------------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
    
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_std_first.set(data[5]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_sname.set(data[6]),
        self.var_std_mid.set(data[7]),
        self.var_address.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_radio1.set(data[10]),
        self.var_sec.set(data[11]),
        self.var_gender.set(data[12]),
        self.var_email.set(data[13]),
        self.var_dob.set(data[14])


    #------------------update function--------------
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_sname.get()=="" or self.var_std_id.get()=="":
            speak_va('Alert!!! All fields are required.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            try:
                speak_va("Do you want to Update this Student's Details?")
                Update=messagebox.askyesno("Update","Do you want to update this details", parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update student set dep=%s,year=%s,firstn=%s,sem=%s,course=%s,surname=%s,midinitial=%s,address=%s,phone=%s,photosample=%s,section=%s,gender=%s,email=%s,birthd=%s where student_id=%s",(

                                                                   self.var_dep.get(),
                                                                   self.var_year.get(),
                                                                   self.var_std_first.get(),
                                                                   self.var_semester.get(),
                                                                   self.var_course.get(),
                                                                   self.var_std_sname.get(),
                                                                   self.var_std_mid.get(),
                                                                   self.var_address.get(),
                                                                   self.var_phone.get(),
                                                                   self.var_radio1.get(),
                                                                   self.var_sec.get(),
                                                                   self.var_gender.get(),
                                                                   self.var_email.get(),
                                                                   self.var_dob.get(),
                                                                   self.var_std_id.get()
                                                                   ))
                else:
                    if not Update:
                        return
                speak_va('Student Details updated successfully.')
                messagebox.showinfo("Success","Student Details updated Successfully.",parent=self.root)                                                                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

#--------------------------delete function------------------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required",parent=self.root)
        else:
            try:
                speak_va("Do you want to Delete this Student's Details?")
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student Details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                conn.close()
                self.fetch_data()
                speak_va('Student Details deleted successfully.')
                self.fetch_data()
                messagebox.showinfo("Delete","Student Details Successfully deleted",parent=self.root)
                self.fetch_data()

            except Exception as es:
                speak_va('An exception occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

#----------------------------------reset function------------------------------------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_sname.set("")
        self.var_std_mid.set("")
        self.var_std_first.set("")
        self.var_sec.set("Select section")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

#------------Generate photo sample -------------

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_sname.get()=="" or self.var_std_id.get()=="":
            speak_va('All Fields are mandatory.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")

                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                new = self.var_std_id.get()
                
                for x in myresult:     
                    id += 1
                my_cursor.execute("update student set dep=%s,year=%s,firstn=%s,sem=%s,course=%s,surname=%s,midinitial=%s,address=%s,phone=%s,photosample=%s,section=%s,gender=%s,email=%s,birthd=%s where student_id=%s",(

                                                                    self.var_dep.get(),
                                                                    self.var_year.get(),
                                                                    self.var_std_first.get(),
                                                                    self.var_semester.get(),
                                                                    self.var_course.get(),
                                                                    self.var_std_sname.get(),
                                                                    self.var_std_mid.get(),
                                                                    self.var_address.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_sec.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_email.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_std_id.get()==id+1
                                                                    ))
                
                print( "idg",self.var_std_id.get())
                self.var_std_id.get()==new
                conn.commit()
                self.fetch_data()
               
                conn.close()
                print(new)
                print( "idg",self.var_std_id.get())
                self.var_std_id.get()==new
                print ("ida:",new)
               
                
             # ------------------load predefined data  face forntal from opencv-----------
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)

                
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face =cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                      #  file_name_path="data/"+str(self.var_roll.get())+"."+str(id)+"."+str(img_id)+".jpg"
                      #   file_name_path="data/"+str(Roll)+"."+str(id)+"."+str(img_id)+".jpg"
       

                        file_name_path="data/"+"user"+"."+str(new)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==20 or int(img_id)==100:
                        break
                   # self.reset_data()
                cap.release()
                cv2.destroyAllWindows()

                speak_va("Generation of Data Set completed.")
                messagebox.showinfo("Result","Generation of data set completed!!!",parent=self.root)
            except Exception as es:
                speak_va("An Exception occurred")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    #==========function================

    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
                
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * from student where " +str(self.var_search.get())+" LIKE '%"+str(self.var_searchtxt.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        speak_va("Data Not Found")
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                speak_va("An Exception Occurred!")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def show_all(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
        
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    

                




 # ________________________________________________________________function____________________________________________________________________________

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()