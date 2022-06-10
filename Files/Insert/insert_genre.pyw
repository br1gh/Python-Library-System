from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
import datetime
import Files.Database

window = Tk()
window.resizable(0, 0)
window.title('Add new genre')
window.configure(background="#1c1c1c")

labels = [
    "Genre:",
]

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


def insert(event=None):
    Files.Database.insert("genres", "(name)", [genre.get()], __file__)

genre = Entry(window, bg='#282828', fg="#eee", insertbackground="#eee", width=40)
genre.focus()
genre.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button1 = Button(window, command=insert, text="Add", bg="#007bff", fg="#fff").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert)

window.mainloop()
