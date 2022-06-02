from tkinter import *
from tkinter import ttk
import Files.Database

show_borrows = Tk()
show_borrows.title('Borrows')

query = "SELECT readers.first_name, readers.last_name, borrow_date, return_date, title, authors.first_name, authors.last_name " \
               "FROM borrows " \
               "INNER JOIN readers ON readers.id = borrows.id_reader " \
               "INNER JOIN copy ON copy.id = borrows.id_copy " \
               "INNER JOIN books ON books.id = copy.id_book " \
               "INNER JOIN authors ON books.id_author = authors.id"

x = Files.Database.select(query)
treeview = ttk.Treeview(show_borrows)
treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_borrows, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('reader_first_name', 'reader_last_name', 'borrow_date', 'return_date', 'title', 'author_first_name', 'author_last_name')

treeview.column("#0", width=0, stretch=NO)
treeview.column("reader_first_name", anchor=CENTER, width=150)
treeview.column("reader_last_name", anchor=CENTER, width=150)
treeview.column("borrow_date", anchor=CENTER, width=150)
treeview.column("return_date", anchor=CENTER, width=150)
treeview.column("title", anchor=CENTER, width=150)
treeview.column("author_first_name", anchor=CENTER, width=150)
treeview.column("author_last_name", anchor=CENTER, width=150)

treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("reader_first_name", text="Reader first name", anchor=CENTER)
treeview.heading("reader_last_name", text="Reader last name", anchor=CENTER)
treeview.heading("borrow_date", text="Borrow date", anchor=CENTER)
treeview.heading("return_date", text="Return date", anchor=CENTER)
treeview.heading("title", text="Title", anchor=CENTER)
treeview.heading("author_first_name", text="Author first name", anchor=CENTER)
treeview.heading("author_last_name", text="Author last name", anchor=CENTER)

for i in x:
    treeview.insert(parent='', index='end', text='', values=i)

show_borrows.mainloop()
