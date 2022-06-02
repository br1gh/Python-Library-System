from tkinter import *
from tkinter import ttk
import Files.Database

show_copies = Tk()
show_copies.title('Copies')

query = "SELECT title, first_name, last_name, available FROM copy " \
"INNER JOIN books ON books.id = copy.id_book " \
"INNER JOIN authors ON books.id_author = authors.id"
x = Files.Database.select(query)
treeview = ttk.Treeview(show_copies)
treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_copies, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('title', 'first_name', 'last_name', 'available')

treeview.column("#0", width=0, stretch=NO)
treeview.column("title", anchor=CENTER, width=150)
treeview.column("first_name", anchor=CENTER, width=150)
treeview.column("last_name", anchor=CENTER, width=150)
treeview.column("available", anchor=CENTER, width=150)

treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("title", text="Title", anchor=CENTER)
treeview.heading("first_name", text="Author first name", anchor=CENTER)
treeview.heading("last_name", text="Author last name", anchor=CENTER)
treeview.heading("available", text="Is available", anchor=CENTER)

for i in x:
    treeview.insert(parent='', index='end', text='', values=i)

show_copies.mainloop()
