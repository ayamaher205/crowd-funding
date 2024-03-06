from tempfile import NamedTemporaryFile
import shutil
import csv
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font


def edition(user):
    edit = Tk()
    edit.title("Registeration Form")
    edit.geometry("850x500+300+100")
    edit['bg'] = '#06283D'
    main_font = Font(family="Times",slant="italic",size="18")
    def update():
        filename = 'projects.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['title', 'details', 'target', 'start date', 'end date']
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['title'] == str(title_input.get()):
                    if row['owner'] == user:
                        print('updating row', row['title'])
                        row['title'], row['details'], row['target'],row['start date'], row['end date'] = new_title_input.get(), details_input.get(), target_input.get(),start_date_input.get(), end_date_input.get()
                row = {'title': row['title'], 'details': row['details'], 'target': row['target'], 'start date': row['start date'],'end date': row['end date']}
                writer.writerow(row)
        shutil.move(tempfile.name, filename)

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
