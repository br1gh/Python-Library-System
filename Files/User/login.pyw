from tkinter import *
from tkinter.ttk import Combobox
import Files.Database


window = Tk()
window.resizable(0, 0)
window.title('Login')
window.configure(background="#1c1c1c")

labels = [
    "Login:",
    "Password:",
]

query1 = "SELECT copy.id, title, first_name, last_name FROM copy " \
         "INNER JOIN books ON copy.id_book = books.id " \
         "INNER JOIN authors ON authors.id = books.id_author"

books = Files.Database.select(query1)

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

def borrow():
    return 0

login = Entry(window, width=40)
login.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

password = Entry(window, show='*', width=40)
password.grid(row=1, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

# if books:
#     list_of_books = dict(zip([i[1] + " by " + i[2] + " " + i[3] for i in books], [i[0] for i in books]))
#     list_of_books_keys = list(list_of_books.keys())
#
#     default_book = StringVar()
#     default_book.set(books[0][1] + " by " + books[0][2] + " " + books[0][3])
#
#     book = Combobox(window, state='readonly', textvariable=default_book, values=list_of_books_keys)
#     book.config(width=37)
#     book.grid(row=0, column=1,sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)
# else:
#     book = Combobox(window, state='disabled')
#     book.config(width=37)
#     book.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)


button = Button(window, command=borrow, text="Login", bg="#007bff", fg="#fff").grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', borrow)

window.mainloop()
