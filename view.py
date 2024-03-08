import csv
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
def view(user):
    def show_project():
        r=50
        projects = csv.DictReader(open('projects.csv', "r"), delimiter=",")
        for row in projects:    
            if row['owner'] == user:
                r+=40
                Label(show, text=row['title'], font=main_font).place(x="100",y=r)
                r+=40
                Label(show, text=row['details'], font=main_font).place(x="100",y=r)
                r+=40
                Label(show, text=row['target'], font=main_font).place(x="100",y=r)
                r+=40
                Label(show, text=row['start date'], font=main_font).place(x="100",y=r)
                r+=40
                Label(show, text=row['end date'], font=main_font).place(x="100",y=r)
    show = Tk()
    show.title("Projects")
    show.geometry("1200x500+100+100")
    show['bg'] = '#06283D'
    main_font = Font(family="Times",slant="italic",size="18")
    show_label = Label(show,text="Your projects are:",font=main_font)
    show_label.place(x="150",y="20")
    show_project()
    show.mainloop()
