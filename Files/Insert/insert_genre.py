from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
import datetime
import Files.Database

insert_books = Tk()
insert_books.title('Add new genre')
insert_books.configure(background="#bbb")

labels = [
    "Genre:",
]

for e, i in enumerate(labels):
    Label(
        insert_books,
        text=labels[e],
        bg='#bbb',
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


genre = Entry(insert_books, width=40).grid(row=0, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)

button = ttk.Button(insert_books, text="Add").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

insert_books.mainloop()
