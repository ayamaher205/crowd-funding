import csv
import json
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
def view(user):
    def show_project():
        projects = csv.DictReader(open('projects.csv', "r"), delimiter=",")
        for row in projects:    
            if row['owner'] == user:
                Label(show, text=row, font=main_font).place(x="100",y="200")
    show = Tk()
    show.title("Show Form")
    show.geometry("1200x500+100+100")
    show['bg'] = '#06283D'
    main_font = Font(family="Times",slant="italic",size="18")
    show_label = Label(show,text="Your projects are:",font=main_font)
    show_label.place(x="150",y="20")
    show_project()
    show.mainloop()
