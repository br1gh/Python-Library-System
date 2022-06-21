import os
from tkinter import *
import Files.Database

import Files.Show.show_authors
import Files.Show.show_books
import Files.Show.show_borrows
import Files.Show.show_copies
import Files.Show.show_genres
import Files.Show.show_readers

import Files.Insert.insert_authors
import Files.Insert.insert_books
import Files.Insert.insert_copies
import Files.Insert.insert_genres

import Files.User.register_user
import Files.User.user


Files.Database.create()

root = Tk()
root.resizable(False, False)
root.title('Library')

def generate_label(root, text, bg, col):
    Label(root, text=text, width=20, bg=bg, fg="#fff", relief='sunken') \
        .grid(row=0, column=col, columnspan=2, sticky=W + E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_content = generate_label(root, "Show content", "#0D47A1", 0)
add_content = generate_label(root, "Add content", "#B71C1C", 2)
user = generate_label(root, "User", "#1B5E20", 4)


show_authors_button = Button(root, command=lambda: Files.Show.show_authors.main())
show_authors_button.configure(text="Show authors", width=20, bg="#1976D2", fg="#fff")
show_authors_button.grid(row=1, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_books_button = Button(root, command=lambda: Files.Show.show_books.main())
show_books_button.configure(text="Show books", width=20, bg="#1976D2", fg="#fff")
show_books_button.grid(row=2, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_borrows_button = Button(root, command=lambda: Files.Show.show_borrows.main())
show_borrows_button.configure(text="Show borrows", width=20, bg="#1976D2", fg="#fff")
show_borrows_button.grid(row=3, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_copies_button = Button(root, command=lambda: Files.Show.show_copies.main())
show_copies_button.configure(text="Show copies", width=20, bg="#1976D2", fg="#fff")
show_copies_button.grid(row=4, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_genres_button = Button(root, command=lambda: Files.Show.show_genres.main())
show_genres_button.configure(text="Show genres", width=20, bg="#1976D2", fg="#fff")
show_genres_button.grid(row=5, column=0, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_readers_button = Button(root, command=lambda: Files.Show.show_readers.main())
show_readers_button.configure(text="Show readers", width=20, bg="#1976D2", fg="#fff")
show_readers_button.grid(row=6, column=0, sticky=W, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)


register_button = Button(root, command=lambda: Files.User.register_user.main())
register_button.configure(text="Register", width=20, bg="#388E3C", fg="#fff")
register_button.grid(row=1, column=4, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

register_button = Button(root, command=lambda: Files.User.user.main())
register_button.configure(text="Login", width=20, bg="#388E3C", fg="#fff")
register_button.grid(row=2, column=4, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)


insert_authors_button = Button(root, command=lambda: Files.Insert.insert_authors.main())
insert_authors_button.configure(text="Add author", width=20, bg="#D32F2F", fg="#fff")
insert_authors_button.grid(row=1, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

insert_books_button = Button(root, command=lambda: Files.Insert.insert_books.main())
insert_books_button.configure(text="Add book", width=20, bg="#D32F2F", fg="#fff")
insert_books_button.grid(row=2, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

insert_copies_button = Button(root, command=lambda: Files.Insert.insert_copies.main())
insert_copies_button.configure(text="Add copy", width=20, bg="#D32F2F", fg="#fff")
insert_copies_button.grid(row=3, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

insert_genres_button = Button(root, command=lambda: Files.Insert.insert_genres.main())
insert_genres_button.configure(text="Add genre", width=20, bg="#D32F2F", fg="#fff")
insert_genres_button.grid(row=4, column=2, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

root.mainloop()
