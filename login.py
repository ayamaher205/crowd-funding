import csv
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from validation import *

login = Tk()
login.title("Login Form")
login.geometry("850x500+300+100")
login['bg'] = '#06283D'  

def login_form():   
    def auth():
        users = csv.reader(open('users.csv', "r"), delimiter=",")
        for row in users:
            if email_input.get() == row[2] and password_input.get() == row[4]:
                return messagebox.showinfo("loggedin","login successfully")
            return messagebox.showerror("error","Wrong password or email")
    main_font = Font(family="Times",slant="italic",size="18")
    email_label = Label(login,text="Enter Email",font=main_font)
    email_label.place(x="150",y="50")
    email_input = Entry(login,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    email_input.place(x="330",y="50")
    password_label = Label(login,text="Enter Password",font=main_font)
    password_label.place(x="150",y="90")
    password_input = Entry(login,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    password_input.place(x="330",y="90")
    login_btn = Button(login, text="Login",width="12", fg="black", bg="#EEDFCC", font=main_font, command=auth)
    login_btn.place(x="350",y="150")
    register_btn = Button(login, text="Register",width="12", fg="black", bg="#EEDFCC", font=main_font)
    register_btn.place(x="350",y="200")
    login.mainloop()
    return email_input.get()
login_form()
