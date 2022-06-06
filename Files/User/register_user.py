from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
import Files.Database




window = Tk()
window.resizable(0, 0)
window.title('Register')
window.configure(background="#1c1c1c")
#
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
        window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]

def generate_entry(root, row, show = ""):
    print(Entry(root, show=show, bg='#282828', fg="#eee", insertbackground="#eee", width=40).grid(row=row, column=1, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5))

email = generate_entry(window, 0)
login = generate_entry(window, 1)
password = generate_entry(window, 2, "*")
confirm_password = generate_entry(window, 3, "*")
first_name = generate_entry(window, 4)
last_name = generate_entry(window, 5)

birth_date = DateEntry(window, width=37, year=date[0], month=date[1], day=date[2],fg="green", tooltipbackground  ='red',
                borderwidth=2).grid(row=6, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

city = generate_entry(window, 7)
street = generate_entry(window, 8)
house_number = generate_entry(window, 9)
phone = generate_entry(window, 10)

button = Button(window, text="Registe", bg="#007bff", fg="#fff").grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

window.mainloop()
