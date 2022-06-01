from tkinter import *
from tkinter import ttk
import Files.Database

show_authors = Tk()
show_authors.title('Readers')

query = "SELECT first_name, last_name, email, birth_date, city, street, house_number, phone FROM readers"
x = Files.Database.select(query)
authors_treeview.pack(side='right')

verscrlbar = ttk.Scrollbar(show_authors, orient="vertical", command=authors_treeview.yview)
verscrlbar.pack(side='right', fill='y')

authors_treeview.configure(yscrollcommand=verscrlbar.set)

authors_treeview = ttk.Treeview(show_authors)

authors_treeview['columns'] = ('first_name', 'last_name', 'email', 'birth_date', 'city', 'street', 'house_number', 'phone')

authors_treeview.column("#0", width=0, stretch=NO)
authors_treeview.column("first_name", anchor=CENTER, width=150)
authors_treeview.column("last_name", anchor=CENTER, width=150)
authors_treeview.column("email", anchor=CENTER, width=150)
authors_treeview.column("birth_date", anchor=CENTER, width=150)
authors_treeview.column("city", anchor=CENTER, width=150)
authors_treeview.column("street", anchor=CENTER, width=150)
authors_treeview.column("house_number", anchor=CENTER, width=150)
authors_treeview.column("phone", anchor=CENTER, width=150)

authors_treeview.heading("#0", text="", anchor=CENTER)
authors_treeview.heading("first_name", text="First name", anchor=CENTER)
authors_treeview.heading("last_name", text="Last name", anchor=CENTER)
authors_treeview.heading("email", text="Email", anchor=CENTER)
authors_treeview.heading("birth_date", text="Birth date", anchor=CENTER)
authors_treeview.heading("city", text="City", anchor=CENTER)
authors_treeview.heading("street", text="Street", anchor=CENTER)
authors_treeview.heading("house_number", text="House number", anchor=CENTER)
authors_treeview.heading("phone", text="Phone", anchor=CENTER)

for i in x:
    authors_treeview.insert(parent='', index='end', text='', values=i)

show_authors.mainloop()
