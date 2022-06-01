from tkinter import *
from tkinter import ttk
import Files.Database

show_authors = Tk()
show_authors.title('Copies')

query = "SELECT name FROM genres"

x = Files.Database.select(query)
authors_treeview = ttk.Treeview(show_authors)

authors_treeview['columns'] = ('name')

authors_treeview.column("#0", width=0, stretch=NO)
authors_treeview.column("name", anchor=CENTER, width=150)

authors_treeview.heading("#0", text="", anchor=CENTER)
authors_treeview.heading("name", text="Genre name", anchor=CENTER)

for i in x:
    authors_treeview.insert(parent='', index='end', text='', values=i)

authors_treeview.pack()
show_authors.mainloop()