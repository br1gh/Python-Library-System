from tkinter import *
from tkinter import ttk
import Files.Database

show_genres = Tk()
show_genres.title('Copies')

query = "SELECT name FROM genres"

x = Files.Database.select(query)
treeview = ttk.Treeview(show_genres)
treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_genres, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('name')

treeview.column("#0", width=0, stretch=NO)
treeview.column("name", anchor=CENTER, width=150)

treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("name", text="Genre name", anchor=CENTER)

for i in x:
    treeview.insert(parent='', index='end', text='', values=i)

show_genres.mainloop()