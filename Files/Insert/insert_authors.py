from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import Files.Database

insert_authors = Tk()
insert_authors.title('Add new author')
insert_authors.configure(background="#bbb")

Label(
    insert_authors,
    text="First name:",
    bg='#bbb',
    ).grid(row=0, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

Label(
    insert_authors,
    text="Last name:",
    bg='#bbb',
    ).grid(row=1, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

Label(
    insert_authors,
    text="Birth date:",
    bg='#bbb',
    ).grid(row=2, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


Entry(insert_authors, width=40).grid(row=0, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)
Entry(insert_authors, width=40).grid(row=1, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)
Entry(insert_authors, width=40).grid(row=2, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)

btn = ttk.Button(insert_authors, text="Add").grid(row=3, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20))


cal = DateEntry(insert_authors, width=12, year=2019, month=6, day=22,
background='darkblue', foreground='white', borderwidth=2).grid(row=4)


insert_authors.mainloop()
