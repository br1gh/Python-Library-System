import Files.Database
from tkinter import *
from tkinter import ttk

dictionary = {
    "readers": ["readers", "(email, login, password, first_name, last_name, birth_date, city, street, house_number, phone)"],
    "authors": ["authors", "(first_name, last_name, birth_date)"],
    "genres": ["genres", "(name)"],
    "books": ["books", "(id_author, id_genre, title, page_number)"],
    "copy": ["copy", "(id_book, available)"],
    "borrows": ["borrows", "(id_reader, id_copy, borrow_date, return_date)"]
}





x = Files.Database.select()

root = Tk()
root.title('Library')
# root['bg'] = '#000'
controlTab = ttk.Notebook(root)

Authors = Frame(controlTab)
Books = Frame(controlTab)

authors_treeview = ttk.Treeview(Authors)

authors_treeview['columns'] = ('first_name', 'last_name', 'birth_date')

authors_treeview.column("#0", width=0,  stretch=NO)
authors_treeview.column("first_name",anchor=CENTER, width=80)
authors_treeview.column("last_name",anchor=CENTER,width=80)
authors_treeview.column("birth_date",anchor=CENTER,width=80)

authors_treeview.heading("#0",text="",anchor=CENTER)
authors_treeview.heading("first_name",text="First Name",anchor=CENTER)
authors_treeview.heading("last_name",text="Last Name",anchor=CENTER)
authors_treeview.heading("birth_date",text="Birth Date",anchor=CENTER)


for i in x:
    authors_treeview.insert(parent='', index='end', iid=0, text='', values=i)

authors_treeview.pack()

controlTab.add(Authors, text='Authors')
controlTab.add(Books, text='Books')
controlTab.pack()


root.mainloop()



# Files.Database.insert(dictionary["authors"], ['Krzysztof', 'Krawczyk', '2022-01-01'])
# Files.Database.insert(dictionary["readers"], ['ok@ok.pl', 'test', 'password', 'first', 'last', '2022-01-20', 'city', 'street', 'number', 'phone'])

# Files.Database.create()
#
# Files.Database.select()
