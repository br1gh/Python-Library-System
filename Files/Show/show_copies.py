from tkinter import *
from tkinter import ttk
import Files.Database

window = Tk()
window.title('Copies')

query = "SELECT title, first_name, last_name, available FROM copy " \
"INNER JOIN books ON books.id = copy.id_book " \
"INNER JOIN authors ON books.id_author = authors.id"
x = Files.Database.select(query)
treeview = ttk.Treeview(window)
treeview.pack(expand=True, side='left', fill='both')

treeview.tag_configure('odd', background='#ddd')
treeview.tag_configure('even', background='#eee')

verscrlbar = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('title', 'first_name', 'last_name', 'available')
columns = [
    ["title", "Title"],
    ["first_name", "Author first name"],
    ["last_name", "Author last name"],
    ["available", "Is available"],
]

treeview.column("#0", width=0, stretch=NO)
treeview.heading("#0", text="", anchor=CENTER)

for i in columns:
    treeview.column(i[0], anchor=CENTER, width=150)
    treeview.heading(i[0], text=i[0], anchor=CENTER)

for e, i in enumerate(x):
    treeview.insert(parent='', index='end', text='', values=i, tags=('odd' if e % 2 == 0 else 'even'))

window.mainloop()
