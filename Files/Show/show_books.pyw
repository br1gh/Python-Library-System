from tkinter import *
from tkinter import ttk
import Files.Database

window = Tk()
window.title('Books')

query = "SELECT title, page_number, first_name, last_name, name FROM books " \
        "INNER JOIN authors ON authors.id = books.id_author " \
        "INNER JOIN genres ON genres.id = books.id_genre"

x = Files.Database.select(query)
treeview = ttk.Treeview(window)
treeview.pack(expand=True, side='left', fill='both')

treeview.tag_configure('odd', background='#ddd')
treeview.tag_configure('even', background='#eee')

verscrlbar = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('title', 'page_number', 'first_name', 'last_name', 'name')

columns = [
    ["title", "Title"],
    ["page_number", "Number of pages"],
    ["first_name", "Author first name"],
    ["last_name", "Author last name"],
    ["name", "Genre"]
]

treeview.column("#0", width=0, stretch=NO)
treeview.heading("#0", text="", anchor=CENTER)

for i in columns:
    treeview.column(i[0], anchor=CENTER, width=150)
    treeview.heading(i[0], text=i[0], anchor=CENTER)

for e, i in enumerate(x):
    treeview.insert(parent='', index='end', text='', values=i, tags=('odd' if e % 2 == 0 else 'even'))

window.mainloop()
