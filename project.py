import json
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

from create import create_project
from delete import deletion
from edit import edition
from search import search_project
from view import view


def crud(user):
    def creation():
        root.destroy()
        create_project(user)

    def edition_project():
        root.destroy()
        edition(user)

    def deletion_project():
        root.destroy()
        deletion(user)
    def search():
        root.destroy()
        search_project(user)

    def show_projects():
        root.destroy()
        view(user)
    root = Tk()
    root.title("Projects profile")
    root.geometry("850x500+300+100")
    root['bg'] = '#06283D'
    main_font = Font(family="Times",slant="italic",size="18")
    create = Button(root, text="Create project",width="12", fg="black", bg="#EEDFCC", font=main_font, command=creation)
    create.place(x="50",y="50")
    delete = Button(root, text="Delete project",width="12", fg="black", bg="#EEDFCC", font=main_font,command=deletion_project)
    delete.place(x="250",y="50")
    show = Button(root, text="Show projects",width="12", fg="black", bg="#EEDFCC", font=main_font,command=show_projects)
    show.place(x="50",y="100")
    edit = Button(root, text="edit projects",width="12", fg="black", bg="#EEDFCC", font=main_font, command=edition_project)
    edit.place(x="250",y="100")
    search = Button(root, text="search for project",width="14", fg="black", bg="#EEDFCC", font=main_font,command=search_project)
    search.place(x="120",y="180")
    root.mainloop()
