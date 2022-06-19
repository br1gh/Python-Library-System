from tkinter import *
from tkinter.ttk import Combobox
import Files.Database
from tkinter import messagebox as msbox
import datetime

window = Tk()
window.resizable(False, False)
window.title('Login')

labels = [
    "Login:",
    "Password:",
]

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

def borrow_db(book, user_id):
    full_date = datetime.datetime.now()
    date = str(full_date.strftime('%Y-%m-%d %H:%M:%S'))
    try:
        Files.Database.insert(
            "borrows", "(id_reader, id_copy, borrow_date)",
            [user_id, book, date],
            __file__)

        Files.Database.update_copy_available(book, 0, __file__)

    except:
        msbox.showinfo('Error', 'Something went wrong')

def return_db(info):
    full_date = datetime.datetime.now()
    date = str(full_date.strftime('%Y-%m-%d %H:%M:%S'))
    try:
        Files.Database.update_return_date(info[0], date, __file__)
        Files.Database.update_copy_available(info[1], 1, __file__)
    except:
        msbox.showinfo('Error', 'Something went wrong')

def borrow_book(user_id):
    borrow_window = Tk()
    borrow_window.resizable(False, False)
    borrow_window.title('Borrow Book')

    available_books = "SELECT copy.id, title, first_name, last_name FROM copy " \
             "INNER JOIN books ON copy.id_book = books.id " \
             "INNER JOIN authors ON authors.id = books.id_author WHERE available = 1"

    books = Files.Database.select(available_books)

    Label(
        borrow_window,
        text='Book: ',
    ).grid(row=0, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

    if books:
        list_of_books = dict(zip([i[1] + " by " + i[2] + " " + i[3] + " (" + str(i[0]) + ")" for i in books], [i[0] for i in books]))
        list_of_books_keys = list(list_of_books.keys())

        book = Combobox(borrow_window, state='readonly', values=list_of_books_keys)
        book.config(width=37)
        book.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)
    else:
        book = Combobox(borrow_window, state='disabled')
        book.config(width=37)
        book.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    borrow_button = Button(borrow_window,
                           command=lambda:
                           borrow_db(list_of_books[book.get()], user_id)
                           if book.get() else
                           msbox.showinfo('Error', "Book field is required! Add book and/or copy if it's disabled"),
                           text="Borrow", bg="#007bff", fg="#fff")
    borrow_button.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    borrow_button.bind('<Return>', borrow_db)

    borrow_window.mainloop()


def return_book(user_id):
    return_window = Tk()
    return_window.resizable(False, False)
    return_window.title('Return Book')

    borrowed_books_query = "SELECT borrows.id, id_copy, title, first_name, last_name, borrow_date, return_date " \
                           "FROM borrows " \
                           "INNER JOIN copy on copy.id = borrows.id_copy " \
                           "INNER JOIN books ON copy.id_book = books.id " \
                           "INNER JOIN authors ON books.id_author = authors.id " \
                           "WHERE id_reader = " + str(user_id) + " AND available = 0 AND return_date IS NULL"

    borrowed_books = Files.Database.select(borrowed_books_query)

    Label(
        return_window,
        text='Book: ',
    ).grid(row=0, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


    if borrowed_books:
        list_borrowed_books = dict(
            zip(
                [i[2] + " by " + i[3] + " " + i[4] + " (" + str(i[1]) + ") (" + i[5] + ")" for i in borrowed_books],
                [i[0:2] for i in borrowed_books])
        )
        list_borrowed_books_keys = list(list_borrowed_books.keys())

        book = Combobox(return_window, state='readonly', values=list_borrowed_books_keys)
        book.config(width=47)
        book.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)
    else:
        book = Combobox(return_window, state='disabled')
        book.config(width=47)
        book.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    return_button = Button(return_window,
                           command=lambda:
                           return_db(list_borrowed_books[book.get()])
                           if book.get() else
                           msbox.showinfo('Error', "Book field is required! No books to return if it's disabled"),
                           text="Return", bg="#007bff", fg="#fff")
    return_button.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    return_button.bind('<Return>', borrow_db)

    return_window.mainloop()


def options(user_id):
    welcome_user_query = "SELECT * FROM readers WHERE id = " + str(user_id)
    readers = Files.Database.select(welcome_user_query)[0]

    options = Tk()
    options.resizable(False, False)
    options.title('User Profile')

    Label(
        options,
        text='Welcome ' + readers[4] + "!",
        bg="#1B5E20", fg="#fff",
    ).grid(row=0, column=0, columnspan=4, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    user_info_labels = [
        "First name:",
        "Last name:",
        "Email:",
        "Birth date:",
        "City:",
        "Street:",
        "House number:",
        "Phone:",
    ]

    user_info_values = [
        readers[4],
        readers[5],
        readers[1],
        readers[6],
        readers[7],
        readers[8],
        readers[9],
        readers[10],
    ]

    for f, _ in enumerate(zip(user_info_labels, user_info_values)):
        Label(
            options,
            text=user_info_labels[f],
        ).grid(row=f+1, column=0, sticky=W, padx=(20, 20), pady=(20, 0))

        Label(
            options,
            text=str(user_info_values[f]),
            borderwidth=2,
            relief="groove"
        ).grid(row=f+1, column=1, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    button_borrow_option = Button(options, width=20, command=lambda: borrow_book(user_id), text="Borrow Book", bg="#007bff", fg="#fff")
    button_borrow_option.grid(row=9, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    button_return_option = Button(options, width=20, command=lambda: return_book(user_id), text="Return Book", bg="#007bff", fg="#fff")
    button_return_option.grid(row=10, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    options.bind('<Return>', borrow_book)
    options.bind('<Return>', return_book)
    options.mainloop()


def login_user():
    query = "SELECT login FROM readers"
    readers = [''.join(i) for i in Files.Database.select(query)]
    if not login.get():
        msbox.showinfo('Error', 'Login field is required')
    if login.get() not in readers:
        msbox.showinfo('Error', 'Incorrect login')
    else:
        query2 = "SELECT id, password FROM readers WHERE login = '" + login.get() + "'"
        password_check = Files.Database.select(query2)
        if password.get() != password_check[0][1]:
            msbox.showinfo('Error', 'Incorrect password')
        else:
            options(password_check[0][0])


login = Entry(window, width=40)
login.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

password = Entry(window, show='*', width=40)
password.grid(row=1, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button = Button(window, command=login_user, text="Login", bg="#007bff", fg="#fff")
button.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', login_user)

window.mainloop()
