from tkinter import *
from tkinter import ttk
import Files.Database

window = Tk()
window.title('Copies')

query = "SELECT name FROM genres"

x = Files.Database.select(query)
treeview = ttk.Treeview(window)

treeview.tag_configure('odd', background='#ddd')
treeview.tag_configure('even', background='#eee')

treeview.pack(expand=True, side='left', fill='both')

verscrlbar = ttk.Scrollbar(window, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('name')

treeview.column("#0", width=0, stretch=NO)
treeview.heading("#0", text="", anchor=CENTER)

treeview.column("name", anchor=CENTER, width=150)
treeview.heading("name", text="Genre name", anchor=CENTER)

for e, i in enumerate(x):
    treeview.insert(parent='', index='end', text='', values=i, tags=('odd' if e % 2 == 0 else 'even'))

window.mainloop()
