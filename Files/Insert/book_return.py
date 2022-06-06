from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
import datetime
import Files.Database

window = Tk()
window.resizable(0, 0)
window.title('Return book')
window.configure(background="#1c1c1c")

labels = [
    "Login:",
    "Password:",
]

query_books = "SELECT books.id, title, first_name, last_name FROM books INNER JOIN authors ON books.id_author = authors.id"
books = Files.Database.select(query_books)

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",

    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]

def generate_entry(row, show = ""):
    return Entry(window, show=show, bg='#282828', fg="#eee", insertbackground="#eee", width=40).grid(row=row, column=1, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

login = generate_entry(0)
password = generate_entry(1, "*")

default_author = StringVar()
default_author.set(books[0][1:3])

button = Button(window, text="Add", bg="#007bff", fg="#fff").grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

window.mainloop()
