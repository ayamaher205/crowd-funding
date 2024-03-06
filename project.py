import json
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

def create():
    root.destroy()
    create = Tk()
    create.title("Registeration Form")
    create.geometry("850x500+300+100")
    create['bg'] = '#06283D'
    title_label = Label(create,text="Enter First Name",bg='white')
    title_label.place(x="100",y="50")
    title_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    title_input.place(x="280",y="50")
    details_label = Label(create,text="Enter Last Name")
    details_label.place(x="100",y="90")
    details_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    details_input.place(x="280",y="90")
    target_label = Label(create,text="Enter Email")
    target_label.place(x="100",y="130")
    target_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    target_input.place(x="280",y="130")
    start_date_label = Label(create,text="Enter Password")
    start_date_label.place(x="100",y="170")
    start_date_input = Entry(create,width="20",show="*",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    start_date_input.place(x="280",y="170")
    end_date_label = Label(create,text="Confirm Password")
    end_date_label.place(x="100",y="210")
    end_date_input = Entry(create,show="*",width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    end_date_input.place(x="280",y="210")
    register = Button(create, text="Register",width="12", fg="black", bg="#EEDFCC", font=main_font)
    register.place(x="320",y="310") 
    create.mainloop() 

def show_projects():
    with open('projects.json') as file:
        projects = json.load(file)
        for project in projects:
            print(project['title'])


root = Tk()
root.title("Registeration Form")
root.geometry("850x500+300+100")
root['bg'] = '#06283D'
main_font = Font(family="Times",slant="italic",size="18")
create = Button(root, text="Create project",width="12", fg="black", bg="#EEDFCC", font=main_font, command=create)
create.place(x="50",y="50")
delete = Button(root, text="Delete project",width="12", fg="black", bg="#EEDFCC", font=main_font)
delete.place(x="250",y="50")
show = Button(root, text="Show projects",width="12", fg="black", bg="#EEDFCC", font=main_font,command=show_projects)
show.place(x="50",y="100")
edit = Button(root, text="edit projects",width="12", fg="black", bg="#EEDFCC", font=main_font)
edit.place(x="250",y="100")
search = Button(root, text="search for project",width="14", fg="black", bg="#EEDFCC", font=main_font)
search.place(x="120",y="180")
root.mainloop()

