import csv
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import shutil
def deletion(user):
    def delete_project():
        with open('projects.csv', "r") as file:
            projects = list(csv.reader(file, delimiter=","))
            for row in projects:
                if row[5] == user:
                    for j in projects:
                        if j[0] == title_input.get() and user == j[5]:
                            with open('projects.csv', 'r') as inp, open('projects_edit.csv', 'w') as out:
                                writer = csv.writer(out)
                                for r in csv.reader(inp):
                                        if r!=j:
                                            writer.writerow(r)
                                        else:
                                            continue
                                shutil.move('projects_edit.csv', 'projects.csv')        
                                return messagebox.showinfo('info', "project deleted successfully")
                    return messagebox.showerror("Error", "project not exist in your projects")
            return messagebox.showerror("authentication","you aren't allowed")
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
    delete_btn.place(x="200",y="150") 
    delete.mainloop()
