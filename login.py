from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import messagebox
import pyttsx3  # pip install pyttsx3
import mysql.connector
from main import Face_Recogniton_System
from main_user import Face_Recogniton_Systems
from mysql.connector import cursor
from logging import root
from os import close

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()



class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        style = ttk.Style()

        self.bg = ImageTk.PhotoImage(file = r"pic\dyci.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1550,height=850)

        frame = Frame(self.root, bg="light blue")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text="Login:", font=("ninito", 20, "bold"),bg= "light blue", fg="black")
        get_str.place(x=125, y=35)

        #Label
        username_lbl = Label(frame, text="Username", font=("ninito", 15, "bold"), bg="light blue", fg="black")
        username_lbl.place(x=40, y=152)

        self.txtuser = ttk.Entry(frame, font=("ninito", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)
      

        password_lbl = Label(frame, text="Password", font=(
        "ninito", 15, "bold"), bg="light blue", fg="black")
        password_lbl.place(x=40, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

          # loginBuutton
        loginbtn = Button(frame, command=self.Face_Recogniton_System, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="blue", fg="black",activeforeground="white",activebackground="dark blue")
        #loginbtn = Button(frame, text="Login", font=("ninito", 15, "bold"), bd=3, relief=RIDGE, bg="blue", fg="black",activeforeground="white",activebackground="dark blue")
        loginbtn.place(x=110, y=350, width=120, height=35)

         # registrationButton
        #registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, bg="green", fg="orange", activebackground="black")
        #registerbtn = Button(frame, text="New User Register", font=("ninito", 8, "bold"), borderwidth=0, bg="light blue", fg="black",activebackground="light blue",activeforeground="red")
        #registerbtn.place(x=40, y=280, width=110)

               # forgetpasswordButton
        #forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, bg="green", fg="orange", activebackground="black")
        #forgetbtn = Button(frame, text="Forget Password",font=("ninito", 8, "bold"),borderwidth=0, bg="light blue", fg="black",activebackground="light blue",activeforeground="red")
        #forgetbtn.place(x=10, y=298, width=160)

    def Face_Recogniton_System(self):
      if self.txtuser.get() == "" or self.txtpass.get() == "":
        messagebox.showerror("Error", "all field required")
      elif self.txtuser.get() == "admin" and self.txtpass.get() == "user@123#":
        speak_va("Welcome to admin main")
        messagebox.showinfo("success", "welcome to admin main")
        self.new_window=Toplevel(self.root)
        self.app=Face_Recogniton_System(self.new_window)

      else:
            conn=mysql.connector.connect(host="localhost", user="root", password="052701brian", database="school")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from users where username=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()

                     ))
            row=my_cursor.fetchone()
            if row==None:
                speak_va("Invalid username and password!")
                messagebox.showerror("Error","Invalid username and password")
            else:
                speak_va("Welcome to user main")
                open_main=messagebox.askyesno("user main","Acess only user  ")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recogniton_Systems(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()  





if __name__ == "__main__":
    root=Tk()
    app=login_window(root) 
    root.mainloop()