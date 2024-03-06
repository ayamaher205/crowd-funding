import csv
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from validation import *

def registeration_form():
    register = Tk()
    register.title("Registeration Form")
    register.geometry("850x500+300+100")
    register['bg'] = '#06283D'
    main_font = Font(family="Times",slant="italic",size="18")

    def validate_data():
            if not validate_name(first_name_input.get()) or not validate_name(last_name_input.get()):
                return messagebox.showerror("Validation Error", "invalid name")
            if not validate_email (email_input.get()):
                return messagebox.showerror("Validation Error", "invalid email address") 
            if not validate_password(password_input.get()):
                return messagebox.showerror("Validation Error", "invalid password: minimum 8 characters password contains a combination of uppercase and lowercase letter , number and special character")
            if confirm_password_input.get()!= password_input.get():
                    return messagebox.showerror("Validation Error","password doesn't match")
            if not validate_phone(phone_input.get()):
                return messagebox.showerror("Validation Error", "invalid phone number")

    def store_data():
     if validate_data() is None:
        data = [first_name_input.get(),last_name_input.get(),email_input.get(),password_input.get(),phone_input.get()]
        with open('users.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        messagebox.showinfo("registeration Status","registered succesfully")      

    
    first_name_label = Label(register,text="Enter First Name",font=main_font)
    first_name_label.place(x="100",y="50")
    first_name_input = Entry(register,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    first_name_input.place(x="320",y="50")
    last_name_label = Label(register,text="Enter Last Name",font=main_font)
    last_name_label.place(x="100",y="90")
    last_name_input = Entry(register,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    last_name_input.place(x="320",y="90")
    email_label = Label(register,text="Enter Email",font=main_font)
    email_label.place(x="100",y="130")
    email_input = Entry(register,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    email_input.place(x="320",y="130")
    password_label = Label(register,text="Enter Password",font=main_font)
    password_label.place(x="100",y="170")
    password_input = Entry(register,width="20",show="*",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    password_input.place(x="320",y="170")
    confirm_password_label = Label(register,text="Confirm Password",font=main_font)
    confirm_password_label.place(x="100",y="210")
    confirm_password_input = Entry(register,show="*",width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    confirm_password_input.place(x="320",y="210")
    phone_label = Label(register,text="Enter Mobile Phone",font=main_font)
    phone_label.place(x="100",y="250")
    phone_input = Entry(register,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    phone_input.place(x="320",y="250")
    register_btn = Button(register, text="Register",width="12", fg="black", bg="#EEDFCC", font=main_font, command=store_data)
    register_btn.place(x="320",y="310")
    register.mainloop()
