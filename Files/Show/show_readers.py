from tkinter import *
from tkinter import ttk
import Files.Database

show_readers = Tk()
show_readers.title('Readers')

query = "SELECT first_name, last_name, email, birth_date, city, street, house_number, phone FROM readers"
x = Files.Database.select(query)
treeview = ttk.Treeview(show_readers)
treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_readers, orient="vertical", command=treeview.yview)
verscrlbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=verscrlbar.set)

treeview['columns'] = ('first_name', 'last_name', 'email', 'birth_date', 'city', 'street', 'house_number', 'phone')

treeview.column("#0", width=0, stretch=NO)
treeview.column("first_name", anchor=CENTER, width=150)
treeview.column("last_name", anchor=CENTER, width=150)
treeview.column("email", anchor=CENTER, width=150)
treeview.column("birth_date", anchor=CENTER, width=150)
treeview.column("city", anchor=CENTER, width=150)
treeview.column("street", anchor=CENTER, width=150)
treeview.column("house_number", anchor=CENTER, width=150)
treeview.column("phone", anchor=CENTER, width=150)

treeview.heading("#0", text="", anchor=CENTER)
treeview.heading("first_name", text="First name", anchor=CENTER)
treeview.heading("last_name", text="Last name", anchor=CENTER)
treeview.heading("email", text="Email", anchor=CENTER)
treeview.heading("birth_date", text="Birth date", anchor=CENTER)
treeview.heading("city", text="City", anchor=CENTER)
treeview.heading("street", text="Street", anchor=CENTER)
treeview.heading("house_number", text="House number", anchor=CENTER)
treeview.heading("phone", text="Phone", anchor=CENTER)

for i in x:
    treeview.insert(parent='', index='end', text='', values=i)

show_readers.mainloop()
