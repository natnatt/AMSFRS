from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  # pip install
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1550x800+0+0")

  # ***************variabletr
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_user = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background img
        self.bg = ImageTk.PhotoImage(file = r"register_img\reg_bg.png")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.bg1 = ImageTk.PhotoImage( file = r"register_img\leftimg.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=115, y=100, width=500, height=550)

         # main frame
        frame = Frame(self.root, bg="light blue")
        frame.place(x=615, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "nonito", 20, "bold"), fg="black", bg="light blue")
        register_lbl.place(x=20, y=20)

        # ***lebal and entry
        # column 1
        fname = Label(frame, text="First Name", font=(
            "source nunito ", 15, "bold"), bg="light blue")
        fname.place(x=70, y=100)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("nonito", 15))
        self.fname_entry.place(x=70, y=130, width=300)

        lname = Label(frame, text="Last Name", font=(
            "nonito", 15, "bold"), bg="light blue")
        lname.place(x=420, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("nonito", 15))
        self.txt_lname.place(x=420, y=130, width=300)

        # column 2
        user = Label(frame, text="User Name", font=(
            "nonito", 15, "bold"), bg="light blue")
        user.place(x=70, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_user, font=("nonito", 15))
        self.txt_contact.place(x=70, y=200, width=300)

        email = Label(frame, text="Email", font=(
            "nonito", 15, "bold"), bg="light blue")
        email.place(x=420, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("nonito", 15))
        self.txt_email.place(x=420, y=200, width=300)



        # ......colum 5
        pswd = Label(frame, text="Password", font=(
            "nonito", 15, "bold"), bg="light blue")
        pswd.place(x=70, y=240)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("nonito", 15))
        self.txt_pswd.place(x=70, y=270, width=300)

        confirm_pswd = Label(frame, text="Confirm Password", font=(
            "nonito", 15, "bold"), bg="light blue")
        confirm_pswd.place(x=420, y=240)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("nonito", 15))
        self.txt_confirm_pswd.place(x=420, y=270, width=300)


        img = Image.open(r"register_img\register.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage, borderwidth=0, cursor="hand2",command=self.register_data)
        b1.place(x=260, y=400, width=200)

    

        # ...............function...................

    def register_data(self):

        if self.var_fname.get() == "" or self.var_user.get() == "":
            messagebox.showerror("Error", "All fills are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="052701brian",database="school")
            my_cursor = conn.cursor()
            query = ("select * from users where username=%s")
            value = (self.var_user.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error", "user already exist ,try another user")
            else:
                my_cursor.execute("insert into users values(%s,%s,%s,%s,%s)", (

                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_user.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_pass.get() 
                ))
                messagebox.showinfo("Success","users Successfully")
            conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()