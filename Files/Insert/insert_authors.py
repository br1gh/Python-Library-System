from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
import Files.Database

insert_authors = Tk()
insert_authors.title('Add new author')
insert_authors.configure(background="#bbb")

labels = [
    "First name:",
    "Last name:",
    "Birth date:"
]

for e, i in enumerate(labels):
    Label(
        insert_authors,
        text=labels[e],
        bg='#bbb',
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]

first_name = Entry(insert_authors, width=40).grid(row=0, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)
last_name = Entry(insert_authors, width=40).grid(row=1, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)

birth_date = DateEntry(insert_authors, width=37, year=date[0], month=date[1], day=date[2], background='#bbb', foreground='#fff',
                borderwidth=2).grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button = ttk.Button(insert_authors, text="Add").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

insert_authors.mainloop()
