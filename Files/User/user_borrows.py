from tkinter import *
from tkinter import ttk
import Files.Database

user_borrows = Tk()
user_borrows.title('Books')

query = "SELECT id_reader, borrow_date, return_date, title, name, authors.first_name, authors.last_name FROM borrows " \
        "INNER JOIN copy ON copy.id = borrows.id_copy " \
        "INNER JOIN books ON copy.id_book = books.id " \
        "INNER JOIN authors ON authors.id = books.id_author " \
        "INNER JOIN genres ON genres.id = books.id_genre " \
        "INNER JOIN readers on readers.id = borrows.id_reader WHERE id_reader=1"

x = Files.Database.select(query)
treeview = ttk.Treeview(user_borrows)
treeview.pack(expand=True, side='left', fill='both')

treeview.tag_configure('odd', background='#ddd')
treeview.tag_configure('even', background='#eee')

verscrlbar = ttk.Scrollbar(user_borrows, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('borrow_date', 'return_date', 'title', 'genre', 'author_first_name', 'author_last_name')

columns = [
    ["borrow_date", "Borrow date"],
    ["return_date", "Return date"],
    ["title", "Title"],
    ["genre", "Genre"],
    ["author_first_name", "Author first name"],
    ["author_last_name", "Author last name"]
]

treeview.column("#0", width=0, stretch=NO)
treeview.heading("#0", text="", anchor=CENTER)

for i in columns:
    treeview.column(i[0], anchor=CENTER, width=150)
    treeview.heading(i[0], text=i[0], anchor=CENTER)

for e, i in enumerate(x):
    treeview.insert(parent='', index='end', text='', values=i, tags=('odd' if e % 2 == 0 else 'even'))

user_borrows.mainloop()
