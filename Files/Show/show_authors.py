from tkinter import *
from tkinter import ttk
import Files.Database

show_authors = Tk()
show_authors.title('Authors')

query = "SELECT first_name, last_name, birth_date FROM authors"

x = Files.Database.select(query)
treeview = ttk.Treeview(show_authors)
treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_authors, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('first_name', 'last_name', 'birth_date')

treeview.column("#0", width=0, stretch=NO)
treeview.column("first_name", anchor=CENTER, width=150)
treeview.column("last_name", anchor=CENTER, width=150)
treeview.column("birth_date", anchor=CENTER, width=150)

treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("first_name", text="First Name", anchor=CENTER)
treeview.heading("last_name", text="Last Name", anchor=CENTER)
treeview.heading("birth_date", text="Birth Date", anchor=CENTER)

for i in x:
    treeview.insert(parent='', index='end', text='', values=i)

show_authors.mainloop()
