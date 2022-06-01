from tkinter import *
from tkinter import ttk
import Files.Database

show_authors = Tk()
show_authors.title('Books')

query = "SELECT title, page_number, first_name, last_name, name FROM books " \
        "INNER JOIN authors ON authors.id = books.id_author " \
        "INNER JOIN genres ON genres.id = books.id_genre"

x = Files.Database.select(query)
authors_treeview = ttk.Treeview(show_authors)

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

authors_treeview.pack()
show_authors.mainloop()
