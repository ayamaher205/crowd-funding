import json
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

def delete_project():
    with open('projects.json') as file:
        projects =json.load(file)
        if not title_input.get() in projects:
            err_label = Label(delete,text=projects['title'],font=main_font)
            err_label.place(x="150",y="200")
delete = Tk()
delete.title("Registeration Form")
delete.geometry("850x500+300+100")
delete['bg'] = '#06283D'
main_font = Font(family="Times",slant="italic",size="18")
delete_label = Label(delete,text="Enter title to delete:",font=main_font)
delete_label.place(x="150",y="20")
title_label = Label(delete,text="Title",font=main_font)
title_label.place(x="150",y="80")
title_input = Entry(delete,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
title_input.place(x="280",y="80")
delete_btn = Button(delete, text="Delete",width="12", fg="white", bg="red", font=main_font,command=delete_project)
delete_btn.place(x="100",y="150") 
delete.mainloop()
