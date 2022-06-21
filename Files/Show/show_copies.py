from tkinter import *
from tkinter import ttk
import Files.Database


def main():
    window = Tk()
    window.title('Copies')

    query = "SELECT copies.id, title, first_name, last_name, available FROM copies " \
    "INNER JOIN books ON books.id = copies.id_book " \
    "INNER JOIN authors ON books.id_author = authors.id"

    x = Files.Database.select(query)
    x = [(i[0:4]) + [('Yes',) if i[4] == 1 else ('No',)][0] for i in x]
    treeview = ttk.Treeview(window)
    treeview.pack(expand=True, side='left', fill='both')

    treeview.tag_configure('odd', background='#ddd')
    treeview.tag_configure('even', background='#eee')

    verscrlbar = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
    verscrlbar.pack(side='right', fill='y')

    treeview.configure(yscrollcommand=verscrlbar.set)

    treeview['columns'] = ('book_id', 'title', 'first_name', 'last_name', 'available')
    columns = [
        ["book_id", "Copy ID"],
        ["title", "Title"],
        ["first_name", "Author first name"],
        ["last_name", "Author last name"],
        ["available", "Is available"],
    ]

    treeview.column("#0", width=0, stretch=NO)
    treeview.heading("#0", text="", anchor=CENTER)

    for i in columns:
        treeview.column(i[0], anchor=CENTER, width=150)
        treeview.heading(i[0], text=i[1], anchor=CENTER)

    for e, i in enumerate(x):
        treeview.insert(parent='', index='end', text='', values=i, tags=('odd' if e % 2 == 0 else 'even'))

    window.mainloop()
