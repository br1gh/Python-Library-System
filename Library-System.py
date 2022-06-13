import datetime
import os
from tkinter import *
from tkinter import ttk
import Files.Database
#
inserts = {
    "borrows": ["borrows", "(id_reader, id_copy, borrow_date, return_date)"]
}

Files.Database.create()

root = Tk()
root.resizable(0, 0)
root.configure(background="#1c1c1c")
root.title('Library')

buttonClicked = False

full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]


def generate_label(root, text, bg, col):
    Label(root, text=text, width=40, bg=bg, fg="#fff") \
        .grid(row=0, column=col, columnspan=2, sticky=W + E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_content = generate_label(root, "Show content", "#0D47A1", 0)
add_content = generate_label(root, "Add content", "#B71C1C", 2)
user = generate_label(root, "User", "#1B5E20", 4)


show_authors_button = Button(root, command=lambda: os.system("start pythonw Files/Show/show_authors.pyw"))
show_authors_button.configure(text="Show authors", width=40, bg="#1976D2", fg="#fff")
show_authors_button.grid(row=1, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_books_button = Button(root, command=lambda: os.system("start pythonw Files/Show/show_books.pyw"))
show_books_button.configure(text="Show books", width=40, bg="#1976D2", fg="#fff")
show_books_button.grid(row=2, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_borrows_button = Button(root, command=lambda: os.system("start pythonw Files/Show/show_borrows.pyw"))
show_borrows_button.configure(text="Show borrows", width=40, bg="#1976D2", fg="#fff")
show_borrows_button.grid(row=3, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_copies_button = Button(root, command=lambda: os.system("start pythonw Files/Show/show_copies.pyw"))
show_copies_button.configure(text="Show copies", width=40, bg="#1976D2", fg="#fff")
show_copies_button.grid(row=4, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_genres_button = Button(root, command=lambda: os.system("start pythonw Files/Show/show_genres.pyw"))
show_genres_button.configure(text="Show genres", width=40, bg="#1976D2", fg="#fff")
show_genres_button.grid(row=5, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_readers_button = Button(root, command=lambda: os.system("start pythonw Files/Show/show_readers.pyw"))
show_readers_button.configure(text="Show readers", width=40, bg="#1976D2", fg="#fff")
show_readers_button.grid(row=6, column=0, sticky=W, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)


register_button = Button(root, command=lambda: os.system("start pythonw Files/User/register_user.pyw"))
register_button.configure(text="Register", width=40, bg="#388E3C", fg="#fff")
register_button.grid(row=1, column=4, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

register_button = Button(root, command=lambda: os.system("start pythonw Files/User/login.pyw"))
register_button.configure(text="Login", width=40, bg="#388E3C", fg="#fff")
register_button.grid(row=2, column=4, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)


insert_authors_button = Button(root, command=lambda: os.system("start pythonw Files/Insert/insert_authors.pyw"))
insert_authors_button.configure(text="Add author", width=40, bg="#D32F2F", fg="#fff")
insert_authors_button.grid(row=1, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

insert_books_button = Button(root, command=lambda: os.system("start pythonw Files/Insert/insert_books.pyw"))
insert_books_button.configure(text="Add book", width=40, bg="#D32F2F", fg="#fff")
insert_books_button.grid(row=2, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

insert_copies_button = Button(root, command=lambda: os.system("start pythonw Files/Insert/insert_copies.pyw"))
insert_copies_button.configure(text="Add copy", width=40, bg="#D32F2F", fg="#fff")
insert_copies_button.grid(row=3, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

insert_genres_button = Button(root, command=lambda: os.system("start pythonw Files/Insert/insert_genre.pyw"))
insert_genres_button.configure(text="Add genre", width=40, bg="#D32F2F", fg="#fff")
insert_genres_button.grid(row=4, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

root.mainloop()
