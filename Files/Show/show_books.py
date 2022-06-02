from tkinter import *
from tkinter import ttk
import Files.Database

show_books = Tk()
show_books.title('Books')

query = "SELECT title, page_number, first_name, last_name, name FROM books " \
        "INNER JOIN authors ON authors.id = books.id_author " \
        "INNER JOIN genres ON genres.id = books.id_genre"

x = Files.Database.select(query)
treeview = ttk.Treeview(show_books)
treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_books, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('title', 'page_number', 'first_name', 'last_name', 'name')

treeview.column("#0", width=0, stretch=NO)
treeview.column("title", anchor=CENTER, width=150)
treeview.column("page_number", anchor=CENTER, width=150)
treeview.column("first_name", anchor=CENTER, width=150)
treeview.column("last_name", anchor=CENTER, width=150)
treeview.column("name", anchor=CENTER, width=150)

treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("title", text="Title", anchor=CENTER)
treeview.heading("page_number", text="Number of pages", anchor=CENTER)
treeview.heading("first_name", text="Author first name", anchor=CENTER)
treeview.heading("last_name", text="Author last name", anchor=CENTER)
treeview.heading("name", text="Genre", anchor=CENTER)

for i in x:
    treeview.insert(parent='', index='end', text='', values=i)

show_books.mainloop()
