from tkinter import *
from tkinter import ttk
import Files.Database


def authors_tab(authors, query):
    x = Files.Database.no_join_select(query)
    authors_treeview = ttk.Treeview(authors)

    authors_treeview['columns'] = ('first_name', 'last_name', 'birth_date')

    authors_treeview.column("#0", width=0, stretch=NO)
    authors_treeview.column("first_name", anchor=CENTER, width=150)
    authors_treeview.column("last_name", anchor=CENTER, width=150)
    authors_treeview.column("birth_date", anchor=CENTER, width=150)

    authors_treeview.heading("#0", text="", anchor=CENTER)
    authors_treeview.heading("first_name", text="First Name", anchor=CENTER)
    authors_treeview.heading("last_name", text="Last Name", anchor=CENTER)
    authors_treeview.heading("birth_date", text="Birth Date", anchor=CENTER)

    for i in x:
        authors_treeview.insert(parent='', index='end', text='', values=i)

    return authors_treeview.pack()


def books_tab(books):
    query = "SELECT title, page_number, first_name, last_name, name FROM books " \
             "INNER JOIN authors ON authors.id = books.id_author " \
             "INNER JOIN genres ON genres.id = books.id_genre"

    x = Files.Database.join_select(query)
    authors_treeview = ttk.Treeview(books)

    authors_treeview['columns'] = ('title', 'page_number', 'first_name', 'last_name', 'name')

    authors_treeview.column("#0", width=0, stretch=NO)
    authors_treeview.column("title", anchor=CENTER, width=150)
    authors_treeview.column("page_number", anchor=CENTER, width=150)
    authors_treeview.column("first_name", anchor=CENTER, width=150)
    authors_treeview.column("last_name", anchor=CENTER, width=150)
    authors_treeview.column("name", anchor=CENTER, width=150)

    authors_treeview.heading("#0", text="", anchor=CENTER)
    authors_treeview.heading("title", text="Title", anchor=CENTER)
    authors_treeview.heading("page_number", text="Number of pages", anchor=CENTER)
    authors_treeview.heading("first_name", text="Author first name", anchor=CENTER)
    authors_treeview.heading("last_name", text="Author last name", anchor=CENTER)
    authors_treeview.heading("name", text="Genre", anchor=CENTER)

    for i in x:
        authors_treeview.insert(parent='', index='end', text='', values=i)

    return authors_treeview.pack()


def borrows_tab(authors):
    query = "SELECT readers.first_name, readers.last_name, borrow_date, return_date, title, authors.first_name, authors.last_name " \
               "FROM borrows " \
               "INNER JOIN readers ON readers.id = borrows.id_reader " \
               "INNER JOIN copy ON copy.id = borrows.id_copy " \
               "INNER JOIN books ON books.id = copy.id_book " \
               "INNER JOIN authors ON books.id_author = authors.id"

    x = Files.Database.join_select(query)
    authors_treeview = ttk.Treeview(authors)

    authors_treeview['columns'] = ('reader_first_name', 'reader_last_name', 'borrow_date', 'return_date', 'title', 'author_first_name', 'author_last_name')

    authors_treeview.column("#0", width=0, stretch=NO)
    authors_treeview.column("reader_first_name", anchor=CENTER, width=150)
    authors_treeview.column("reader_last_name", anchor=CENTER, width=150)
    authors_treeview.column("borrow_date", anchor=CENTER, width=150)
    authors_treeview.column("return_date", anchor=CENTER, width=150)
    authors_treeview.column("title", anchor=CENTER, width=150)
    authors_treeview.column("author_first_name", anchor=CENTER, width=150)
    authors_treeview.column("author_last_name", anchor=CENTER, width=150)

    authors_treeview.heading("#0", text="", anchor=CENTER)
    authors_treeview.heading("reader_first_name", text="Reader first name", anchor=CENTER)
    authors_treeview.heading("reader_last_name", text="Reader last name", anchor=CENTER)
    authors_treeview.heading("borrow_date", text="Borrow date", anchor=CENTER)
    authors_treeview.heading("return_date", text="Return date", anchor=CENTER)
    authors_treeview.heading("title", text="Title", anchor=CENTER)
    authors_treeview.heading("author_first_name", text="Author first name", anchor=CENTER)
    authors_treeview.heading("author_last_name", text="Author last name", anchor=CENTER)

    for i in x:
        authors_treeview.insert(parent='', index='end', text='', values=i)

    return authors_treeview.pack()


def copy_tab(copy):
    query = "SELECT title, first_name, last_name, available FROM copy " \
    "INNER JOIN books ON books.id = copy.id_book " \
    "INNER JOIN authors ON books.id_author = authors.id"
    x = Files.Database.join_select(query)
    authors_treeview = ttk.Treeview(copy)

    authors_treeview['columns'] = ('title', 'first_name', 'last_name', 'available')

    authors_treeview.column("#0", width=0, stretch=NO)
    authors_treeview.column("title", anchor=CENTER, width=150)
    authors_treeview.column("first_name", anchor=CENTER, width=150)
    authors_treeview.column("last_name", anchor=CENTER, width=150)
    authors_treeview.column("available", anchor=CENTER, width=150)

    authors_treeview.heading("#0", text="", anchor=CENTER)
    authors_treeview.heading("title", text="Title", anchor=CENTER)
    authors_treeview.heading("first_name", text="Author first name", anchor=CENTER)
    authors_treeview.heading("last_name", text="Author last name", anchor=CENTER)
    authors_treeview.heading("available", text="Is available", anchor=CENTER)

    for i in x:
        authors_treeview.insert(parent='', index='end', text='', values=i)

    return authors_treeview.pack()


def genres_tab(authors, query):
    x = Files.Database.no_join_select(query)
    authors_treeview = ttk.Treeview(authors)

    authors_treeview['columns'] = ('name')

    authors_treeview.column("#0", width=0, stretch=NO)
    authors_treeview.column("name", anchor=CENTER, width=150)

    authors_treeview.heading("#0", text="", anchor=CENTER)
    authors_treeview.heading("name", text="Genre name", anchor=CENTER)

    for i in x:
        authors_treeview.insert(parent='', index='end', text='', values=i)

    return authors_treeview.pack()

def readers_tab(authors):

    query = "SELECT first_name, last_name, email, birth_date, city, street, house_number, phone FROM readers"

    x = Files.Database.join_select(query)
    authors_treeview = ttk.Treeview(authors)

    authors_treeview['columns'] = ('first_name', 'last_name', 'email', 'birth_date', 'city', 'street', 'house_number', 'phone')

    authors_treeview.column("#0", width=0, stretch=NO)
    authors_treeview.column("first_name", anchor=CENTER, width=150)
    authors_treeview.column("last_name", anchor=CENTER, width=150)
    authors_treeview.column("email", anchor=CENTER, width=150)
    authors_treeview.column("birth_date", anchor=CENTER, width=150)
    authors_treeview.column("city", anchor=CENTER, width=150)
    authors_treeview.column("street", anchor=CENTER, width=150)
    authors_treeview.column("house_number", anchor=CENTER, width=150)
    authors_treeview.column("phone", anchor=CENTER, width=150)

    authors_treeview.heading("#0", text="", anchor=CENTER)
    authors_treeview.heading("first_name", text="First name", anchor=CENTER)
    authors_treeview.heading("last_name", text="Last name", anchor=CENTER)
    authors_treeview.heading("email", text="Email", anchor=CENTER)
    authors_treeview.heading("birth_date", text="Birth date", anchor=CENTER)
    authors_treeview.heading("city", text="City", anchor=CENTER)
    authors_treeview.heading("street", text="Street", anchor=CENTER)
    authors_treeview.heading("house_number", text="House number", anchor=CENTER)
    authors_treeview.heading("phone", text="Phone", anchor=CENTER)

    for i in x:
        authors_treeview.insert(parent='', index='end', text='', values=i)

    return authors_treeview.pack()
