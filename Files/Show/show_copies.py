from tkinter import *
from tkinter import ttk
import Files.Database

show_authors = Tk()
show_authors.title('Copies')

query = "SELECT title, first_name, last_name, available FROM copy " \
"INNER JOIN books ON books.id = copy.id_book " \
"INNER JOIN authors ON books.id_author = authors.id"
x = Files.Database.select(query)
authors_treeview = ttk.Treeview(show_authors)

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

authors_treeview.pack()
show_authors.mainloop()
