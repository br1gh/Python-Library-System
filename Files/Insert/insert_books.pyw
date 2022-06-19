from tkinter import *
from tkinter.ttk import Combobox
import Files.Database
from tkinter import messagebox as msbox

window = Tk()
window.resizable(False, False)
window.title('Add new book')

labels = [
    "Title:",
    "Number of pages:",
    "Author:",
    "Genre:"
]

query_authors = "SELECT id, first_name, last_name FROM authors"
authors = Files.Database.select(query_authors)

query_authors = "SELECT id, name FROM genres"
genres = Files.Database.select(query_authors)

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

def insert_book():
    if not authors or not author.get():
        msbox.showinfo('Error', "Author field is required! Add the new one if it's disabled")
    elif not genres or not genre.get():
        msbox.showinfo('Error', "Genre field is required! Add the new one if it's disabled")
    elif not title.get():
        msbox.showinfo('Error', 'Title field is required')
    elif not number_of_pages.get():
        msbox.showinfo('Error', 'Number of pages field is required')
    else:
        try:
            x = int(number_of_pages.get())
        except:
            msbox.showinfo('Error', 'Number of pages field must be an integer')
        else:
            if x < 1:
                msbox.showinfo('Error', 'Number of pages field must be greater than 0')
            else:
                Files.Database.insert(
                    "books", "(id_author, id_genre, title, page_number)",
                    [list_of_authors[author.get()], list_of_genres[genre.get()], title.get(), x],
                    __file__)
                msbox.showinfo('Success', 'Book has been added')


title = Entry(window, width=40)
title.grid(row=0, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)
number_of_pages = Entry(window, width=40)
number_of_pages.grid(row=1, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)


if authors:
    list_of_authors = dict(zip([i[1] + ' ' + i[2] for i in authors], [i[0] for i in authors]))
    list_of_authors_keys = list(list_of_authors.keys())

    default_author = StringVar()
    default_author.set(list_of_authors_keys[0])
    author = Combobox(window, state='readonly', textvariable=default_author, values=list(list_of_authors_keys))
    author.config(width=37)
    author.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)
else:
    author = Combobox(window, state='disabled')
    author.config(width=37)
    author.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)


if genres:
    list_of_genres = dict(zip([i[1] for i in genres], [i[0] for i in genres]))
    list_of_genres_keys = list(list_of_genres.keys())

    default_genre = StringVar()
    default_genre.set(list_of_genres_keys[0])
    genre = Combobox(window, state='readonly', textvariable=default_genre, values=list(list_of_genres_keys))
    genre.config(width=37)
    genre.grid(row=3, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)
else:
    genre = Combobox(window, state='disabled')
    genre.config(width=37)
    genre.grid(row=3, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)


button = Button(window, command=insert_book, text="Add book", bg="#007bff", fg="#fff").grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert_book)

window.mainloop()
