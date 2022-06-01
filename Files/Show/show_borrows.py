from tkinter import *
from tkinter import ttk
import Files.Database

show_authors = Tk()
show_authors.title('Borrows')

query = "SELECT readers.first_name, readers.last_name, borrow_date, return_date, title, authors.first_name, authors.last_name " \
               "FROM borrows " \
               "INNER JOIN readers ON readers.id = borrows.id_reader " \
               "INNER JOIN copy ON copy.id = borrows.id_copy " \
               "INNER JOIN books ON books.id = copy.id_book " \
               "INNER JOIN authors ON books.id_author = authors.id"

x = Files.Database.select(query)
authors_treeview = ttk.Treeview(show_authors)
authors_treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_authors, orient="vertical", command=authors_treeview.yview)
verscrlbar.pack(side='right', fill='y')

authors_treeview.configure(yscrollcommand=verscrlbar.set)

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

show_authors.mainloop()
