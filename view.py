import json
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

def search_for_project():
    with open('projects.json') as file:
        projects =json.load(file)
        if not title_input.get() in projects:
            err_label = Label(search,text=projects['title'],font=main_font)
            err_label.place(x="150",y="200")
search = Tk()
search.title("Registeration Form")
search.geometry("850x500+300+100")
search['bg'] = '#06283D'
main_font = Font(family="Times",slant="italic",size="18")
search_label = Label(search,text="Enter title to search for:",font=main_font)
search_label.place(x="150",y="20")
title_label = Label(search,text="Title",font=main_font)
title_label.place(x="150",y="80")
title_input = Entry(search,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
title_input.place(x="280",y="80")
search_btn = Button(search, text="Create",width="12", fg="black", bg="#EEDFCC", font=main_font,command=search_for_project)
search_btn.place(x="100",y="150") 
search.mainloop()
