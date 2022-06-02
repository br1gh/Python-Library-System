from tkinter import *
from tkinter import ttk
import Files.Database

insert_authors = Tk()
insert_authors.title('Add new author')
insert_authors.configure(background="#bbb")

Label(
    insert_authors,
    text="First name",
    bg='#CCCCCC',
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    insert_authors,
    text="Last name",
    bg='#CCCCCC',
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    insert_authors,
    text="Birth date",
    bg='#CCCCCC',
    ).grid(row=2, column=0, sticky=W, pady=10)

insert_authors.mainloop()
