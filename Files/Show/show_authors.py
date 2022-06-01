from tkinter import *
from tkinter import ttk
import Files.Database

show_authors = Tk()
show_authors.title('Authors')

query = "SELECT first_name, last_name, birth_date FROM authors"

x = Files.Database.select(query)
authors_treeview = ttk.Treeview(show_authors)

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

authors_treeview.pack()
show_authors.mainloop()
