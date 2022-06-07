from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
import Files.Database


login_window = Tk()
login_window.resizable(0, 0)
login_window.title('Login')
login_window.configure(background="#1c1c1c")
#
labels = [
    "Email:",
    "Login:",
    "Password:",
]

query_books = "SELECT books.id, title, first_name, last_name FROM books INNER JOIN authors ON books.id_author = authors.id"
books = Files.Database.select(query_books)


for e, i in enumerate(labels):
    Label(
        login_window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]

def generate_entry(root, row, show = ""):
    print(Entry(root, show=show, bg='#282828', fg="#eee", insertbackground="#eee", width=40).grid(row=row, column=1, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5))

email = generate_entry(login_window, 0)
login = generate_entry(login_window, 1)
password = generate_entry(login_window, 2, "*")

def show_options():
    path = "Files/User/options.py" if "Library-System.py" in __file__ else "options.py"
    exec(open(path).read())


button = Button(login_window, text="Login", command=show_options ,bg="#007bff", fg="#fff").grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

login_window.mainloop()
