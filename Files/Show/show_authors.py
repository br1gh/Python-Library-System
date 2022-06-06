from tkinter import *
from tkinter import ttk
import Files.Database

window = Tk()
window.title('Authors')

query = "SELECT first_name, last_name, birth_date FROM authors"

x = Files.Database.select(query)
treeview = ttk.Treeview(window)

treeview.tag_configure('odd', background='#ddd')
treeview.tag_configure('even', background='#eee')

treeview.pack(expand=True, side='left', fill='both')

verscrlbar = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('first_name', 'last_name', 'birth_date')
columns = [
    ["first_name", "First Name"],
    ["last_name", "Last Name"],
    ["birth_date", "Birth Date"]
]

treeview.column("#0", width=0, stretch=NO)
treeview.heading("#0", text="", anchor=CENTER)

for i in columns:
    treeview.column(i[0], anchor=CENTER, width=150)
    treeview.heading(i[0], text=i[0], anchor=CENTER)

for e, i in enumerate(x):
    treeview.insert(parent='', index='end', text='', values=i, tags=('odd' if e % 2 == 0 else 'even'))

window.mainloop()
