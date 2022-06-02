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
treeview.pack(expand=True, side='left', fill='both')

treeview.tag_configure('odd', background='#ddd')
treeview.tag_configure('even', background='#eee')

verscrlbar = ttk.Scrollbar(show_borrows, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('reader_first_name', 'reader_last_name', 'borrow_date', 'return_date', 'title', 'author_first_name', 'author_last_name')

columns = [
    ["reader_first_name", "Reader first name"],
    ["reader_last_name", "Reader last name"],
    ["borrow_date", "Borrow date"],
    ["return_date", "Return date"],
    ["title", "Title"],
    ["author_first_name", "Author first name"],
    ["author_last_name", "Author last name"],
]

treeview.column("#0", width=0, stretch=NO)
treeview.heading("#0", text="", anchor=CENTER)

for i in columns:
    treeview.column(i[0], anchor=CENTER, width=150)
    treeview.heading(i[0], text=i[0], anchor=CENTER)

for e, i in enumerate(x):
    treeview.insert(parent='', index='end', text='', values=i, tags=('odd' if e % 2 == 0 else 'even'))

show_borrows.mainloop()
