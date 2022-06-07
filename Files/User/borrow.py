from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
import datetime
import Files.Database

window = Tk()
window.resizable(0, 0)
window.title('Add new copy')
window.configure(background="#1c1c1c")

labels = [
    "Book:",
]

query_books = "SELECT copy.id, title, first_name, last_name FROM copy " \
        "INNER JOIN books on books.id = copy.id_book " \
        "INNER JOIN authors ON authors.id = books.id_author WHERE available = 1"
books = Files.Database.select(query_books)


for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

default_author = StringVar()
default_author.set(books[0][1] + " by " + books[0][2] + " " + books[0][3])

author = Combobox(window,textvariable=default_author, values=[i[1] + " by " + i[2] + " " + i[3] + " (" + str(i[0]) + ")" for i in books])
author.config(width=37)
author.grid(row=0, column=1,sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button = Button(window, text="Add", command=lambda: print("aa"), bg="#007bff", fg="#fff").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

window.mainloop()

