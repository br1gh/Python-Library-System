from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
import datetime
import Files.Database

insert_books = Tk()
insert_books.title('Register')
insert_books.configure(background="#1c1c1c")

labels = [
    "Email:",
    "Login:",
    "Password:",
    "Confirm password:",
    "First name:",
    "Last name:",
    "Birth date:",
    "City:",
    "Street:",
    "House number:",
    "Phone:",
]

query_books = "SELECT books.id, title, first_name, last_name FROM books INNER JOIN authors ON books.id_author = authors.id"
books = Files.Database.select(query_books)


for e, i in enumerate(labels):
    Label(
        insert_books,
        text=labels[e],
        fg="#eeeeee",
        bg="#1c1c1c",

    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]

def generate_entry(row, show = ""):
    return Entry(insert_books, show=show, bg='#282828', fg="#eee", insertbackground="#eee", width=40).grid(row=row, column=1, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

email = generate_entry(0)
login = generate_entry(1)
password = generate_entry(2, "*")
confirm_password = generate_entry(3, "*")
first_name = generate_entry(4)
last_name = generate_entry(5)

birth_date = DateEntry(insert_books, width=37, year=date[0], month=date[1], day=date[2],fg="green", tooltipbackground  ='red',
                borderwidth=2).grid(row=6, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

city = generate_entry(7)
street = generate_entry(8)
house_number = generate_entry(9)
phone = generate_entry(10)

button = ttk.Button(insert_books, text="Add").grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

insert_books.mainloop()
