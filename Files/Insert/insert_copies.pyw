from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox as msbox
from tkcalendar import DateEntry
import datetime
import Files.Database

window = Tk()
window.resizable(0, 0)
window.title('Add new copy')
window.configure(background="#1c1c1c")

def insert_copies():
    if not books or not book.get():
        msbox.showinfo('Error', "Author field is required! Add the new one if it's disabled")
    else:
        try:
            x = int(amount.get())
        except:
            msbox.showinfo('Error', 'Amount field must be a number')
        else:
            for _ in range(x):
                Files.Database.insert(
                    "copy", "(id_book, available)", [list_of_books[book.get()], 1], __file__)
            msbox.showinfo('Success', 'Added ' + str(x) + ' copies of this book')

labels = [
    "Book:",
    "Amount:",
]

query_books = "SELECT books.id, title, first_name, last_name FROM books " \
              "INNER JOIN authors ON books.id_author = authors.id"
books = Files.Database.select(query_books)


for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


title = Entry(window, width=40)
title.grid(row=0, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)
amount = Entry(window, width=40)
amount.grid(row=1, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)

if books:
    list_of_books = dict(zip([i[1] + " by " + i[2] + " " + i[3] for i in books], [i[0] for i in books]))
    list_of_books_keys = list(list_of_books.keys())

    default_book = StringVar()
    default_book.set(books[0][1] + " by " + books[0][2] + " " + books[0][3])

    book = Combobox(window, state='readonly', textvariable=default_book, values=list_of_books_keys)
    book.config(width=37)
    book.grid(row=0, column=1,sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)
else:
    book = Combobox(window, state='disabled')
    book.config(width=37)
    book.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)


button = Button(window, command=insert_copies, text="Add copy", bg="#007bff", fg="#fff").grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert_copies)

window.mainloop()
