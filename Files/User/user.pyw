from tkinter import *
from tkinter.ttk import Combobox
import Files.Database
from tkinter import messagebox as msbox
import datetime


def borrow_db(book, user_id):
    full_date = datetime.datetime.now()
    date = str(full_date.strftime('%Y-%m-%d %H:%M:%S'))

    try:
        Files.Database.insert(
            "borrows", "(id_reader, id_copy, borrow_date)",
            [user_id, book, date],
            __file__)

        Files.Database.update_copy_available(book, 0, __file__)

        msbox.showinfo('Success', 'Book has been borrowed')

    except:
        msbox.showerror('Error', 'Something went wrong')

def return_db(info):
    full_date = datetime.datetime.now()
    date = str(full_date.strftime('%Y-%m-%d %H:%M:%S'))

    try:
        Files.Database.update_return_date(info[0], date, __file__)
        Files.Database.update_copy_available(info[1], 1, __file__)

        msbox.showinfo('Success', 'Book has been returned')

    except:
        msbox.showerror('Error', 'Something went wrong')


def borrow_book(user_id):
    borrow_window = Tk()
    borrow_window.resizable(False, False)
    borrow_window.title('Borrow Book')

    available_books_query = "SELECT copy.id, title, first_name, last_name FROM copy " \
        "INNER JOIN books ON copy.id_book = books.id " \
        "INNER JOIN authors ON authors.id = books.id_author WHERE available = 1"

    available_books = Files.Database.select(available_books_query)

    Label(
        borrow_window,
        text='Book: ',
    ).grid(row=0, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

    book = Combobox(borrow_window, width=97)
    book.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    if available_books:
        list_of_books = dict(zip(
            [i[1] + " by " + i[2] + " " + i[3] + " (" + str(i[0]) + ")" for i in available_books],
            [i[0] for i in available_books]
        ))

        list_of_books_keys = list(list_of_books.keys())

        book.config(state='readonly', values=list_of_books_keys)

    else:
        book.config(state='disabled')

    borrow_button = Button(
        borrow_window,
        command=lambda: borrow_db(list_of_books[book.get()], user_id) if book.get()
        else msbox.showerror('Error', "Book is required! Add book and/or copy if field is disabled"),
        text="Borrow", bg="#388E3C", fg="#fff"
    )

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

    book = Combobox(return_window, width=97)
    book.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    if borrowed_books:
        list_borrowed_books = dict(zip(
                [i[2] + " by " + i[3] + " " + i[4] + " (" + str(i[1]) + ") (" + i[5] + ")" for i in borrowed_books],
                [i[0:2] for i in borrowed_books]
            ))
        list_borrowed_books_keys = list(list_borrowed_books.keys())

        book.config(state='readonly', values=list_borrowed_books_keys)

    else:
        book.config(state='disabled')

    return_button = Button(
        return_window,
        command=lambda: return_db(list_borrowed_books[book.get()]) if book.get()
        else msbox.showerror('Error', "Book is required! No books to return if field is disabled"),
        text="Return", bg="#388E3C", fg="#fff"
    )

    return_button.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    return_button.bind('<Return>', borrow_db)

    return_window.mainloop()


def user_profile(user_id):
    user_info_query = "SELECT * FROM readers WHERE id = " + str(user_id)
    user_info = Files.Database.select(user_info_query)[0]

    profile_window = Tk()
    profile_window.resizable(False, False)
    profile_window.title('User Profile')

    Label(
        profile_window,
        text='Welcome ' + user_info[4] + "!",
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
        user_info[4],
        user_info[5],
        user_info[1],
        user_info[6],
        user_info[7],
        user_info[8],
        user_info[9],
        user_info[10],
    ]

    for f, _ in enumerate(zip(user_info_labels, user_info_values)):
        Label(
            profile_window,
            text=user_info_labels[f],
        ).grid(row=f+1, column=0, sticky=W, padx=(20, 20), pady=(20, 0))

        Label(
            profile_window,
            text=str(user_info_values[f]),
            borderwidth=2,
            relief="groove"
        ).grid(row=f+1, column=1, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    borrow_option_btn = Button(
        profile_window, width=20,
        command=lambda: borrow_book(user_id),
        text="Borrow Book", bg="#388E3C", fg="#fff"
    )

    borrow_option_btn.grid(row=9, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    return_option_btn = Button(
        profile_window, width=20, command=lambda: return_book(user_id),
        text="Return Book", bg="#388E3C", fg="#fff"
    )

    return_option_btn.grid(row=10, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

    profile_window.bind('<Return>', borrow_book)
    profile_window.bind('<Return>', return_book)
    profile_window.mainloop()


def login_user():
    logins_query = "SELECT login FROM readers"
    logins = [''.join(i) for i in Files.Database.select(logins_query)]

    if not login.get():
        msbox.showerror('Error', 'Login is required')

    elif not password.get():
        msbox.showerror('Error', 'Password is required')

    elif login.get() not in logins:
        msbox.showerror('Error', 'Incorrect login')

    else:
        password_query = "SELECT id, password FROM readers WHERE login = '" + login.get() + "'"
        password_check = Files.Database.select(password_query)

        if password.get() != password_check[0][1]:
            msbox.showerror('Error', 'Incorrect password')

        else:
            user_profile(password_check[0][0])


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

login = Entry(window, width=40)
login.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

password = Entry(window, show='*', width=40)
password.grid(row=1, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

login_btn = Button(window, command=login_user, text="Login", bg="#388E3C", fg="#fff")
login_btn.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', login_user)

window.mainloop()
