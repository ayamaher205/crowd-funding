import csv
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

from validation import validate_date
    
def create_project():            
      def store_data():
            if not validate_date(start_date_input.get()) is None or not validate_date(end_date_input.get()) is None:
                  return messagebox.showerror("validation Error","Incorrect data format, date should be YYYY-MM-DD")
            data = [title_input.get(),details_input.get(),target_input.get(),start_date_input.get(),end_date_input.get()]
            with open('projects.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow(data)
      create = Tk()
      create.title("Registeration Form")
      create.geometry("850x500+300+100")
      create['bg'] = '#06283D'
      main_font = Font(family="Times",slant="italic",size="18")
      title_label = Label(create,text="Title",font=main_font)
      title_label.place(x="100",y="50")
      title_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
      title_input.place(x="280",y="50")
      details_label = Label(create,text="Details",font=main_font)
      details_label.place(x="100",y="90")
      details_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
      details_input.place(x="280",y="90")
      target_label = Label(create,text="Target",font=main_font)
      target_label.place(x="100",y="130")
      target_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
      target_input.place(x="280",y="130")
      start_date_label = Label(create,text="Start Date",font=main_font)
      start_date_label.place(x="100",y="170")
      start_date_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
      start_date_input.place(x="280",y="170")
      end_date_label = Label(create,text="End Date", font=main_font)
      end_date_label.place(x="100",y="210")
      end_date_input = Entry(create,width="20",fg="#080808",bg="#EEDFCC",font=main_font,borderwidth="2")
      end_date_input.place(x="280",y="210")
      add = Button(create, text="Create",width="12", fg="black", bg="#EEDFCC", font=main_font,command=store_data)
      add.place(x="320",y="310") 
      create.mainloop()
