from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
import datetime
import Files.Database

insert_books = Tk()
insert_books.title('Add new copy')
insert_books.configure(background="#bbb")

labels = [
    "Book:",
    "Amount:",

]

query_books = "SELECT books.id, title, first_name, last_name FROM books INNER JOIN authors ON books.id_author = authors.id"
books = Files.Database.select(query_books)


for e, i in enumerate(labels):
    Label(
        insert_books,
        text=labels[e],
        bg='#bbb',
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


title = Entry(insert_books, width=40).grid(row=0, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)
number_of_pages = Entry(insert_books, width=40).grid(row=1, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)


default_author = StringVar()
default_author.set(books[0][1] + " by " + books[0][2] + " " + books[0][3])

author = Combobox(insert_books,textvariable=default_author, values=[i[1] + " by " + i[2] + " " + i[3] for i in books])
author.config(width=37)
author.grid(row=0, column=1,sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button = ttk.Button(insert_books, text="Add").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

insert_books.mainloop()
