from tempfile import NamedTemporaryFile
import csv
from csv import *
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font


def edition(user):
    edit = Tk()
    edit.title("Update Project")
    edit.geometry("850x500+300+100")
    edit['bg'] = '#06283D'
    main_font = Font(family="Times",slant="italic",size="18")
    def update():
        filename = 'projects.csv'
        updated = False
        
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            projects = list(reader)
        
        for project in projects:
            if project['title'] == title_input.get() and project['owner'] == user:
                project['title'] = project['title'] if new_title_input.get().strip()== '' else new_title_input.get().strip()
                project['details'] = details_input.get().strip() if details_input.get().strip()!='' else project['details']
                project['target'] = target_input.get().strip() if target_input.get().strip() != '' else project['target']
                project['start date'] = start_date_input.get().strip() if start_date_input.get().strip() != '' else project['start date']
                project['end date'] = end_date_input.get().strip() if end_date_input.get().strip() != '' else project['end date']
                updated = True
                break  
        
        if updated:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['title', 'details', 'target', 'start date', 'end date', 'owner']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(projects)
            messagebox.showinfo("Success","Project updated successfully")
        else:
            messagebox.showerror("Error","Project with title '{}' not found".format(title_input.get()))


    edit_label = Label(edit,text="Enter title of project to update:",font=main_font)
    edit_label.place(x="100",y="20")
    title_label = Label(edit,text="Title",font=main_font)
    title_label.place(x="100",y="80")
    title_input = Entry(edit,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    title_input.place(x="280",y="80")
    edit_label = Label(edit,text="Enter new data of project to update:",font=main_font)
    edit_label.place(x="100",y="120")
    new_title_label = Label(edit,text="Title",font=main_font)
    new_title_label.place(x="100",y="150")
    new_title_input = Entry(edit,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    new_title_input.place(x="280",y="150")
    details_label = Label(edit,text="Details",font=main_font)
    details_label.place(x="100",y="190")
    details_input = Entry(edit,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    details_input.place(x="280",y="190")
    target_label = Label(edit,text="Target",font=main_font)
    target_label.place(x="100",y="230")
    target_input = Entry(edit,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    target_input.place(x="280",y="230")
    start_date_label = Label(edit,text="Start Date",font=main_font)
    start_date_label.place(x="100",y="270")
    start_date_input = Entry(edit,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    start_date_input.place(x="280",y="270")
    end_date_label = Label(edit,text="End Date", font=main_font)
    end_date_label.place(x="100",y="310")
    end_date_input = Entry(edit,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
    end_date_input.place(x="280",y="310")
    add = Button(edit, text="edit",width="12", fg="black", bg="#EEDFCC", font=main_font,command=update)
    add.place(x="320",y="350") 
    edit.mainloop()
