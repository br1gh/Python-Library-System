from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msbox
import Files.Database


def insert_book():
    if not authors or not author.get():
        msbox.showerror('Error', "Author is required! Add the new one if field is disabled")

    elif not genres or not genre.get():
        msbox.showerror('Error', "Genre is required! Add the new one if field is disabled")

    elif not title.get():
        msbox.showerror('Error', 'Title is required')

    elif not number_of_pages.get():
        msbox.showerror('Error', 'Number of pages is required')

    else:
        try:
            pages_int = int(number_of_pages.get())

        except:
            msbox.showerror('Error', 'Number of pages must be an integer')

        else:
            if pages_int < 1:
                msbox.showerror('Error', 'Number of pages must be greater than 0')

            else:
                try:
                    Files.Database.insert(
                        "books", "(id_author, id_genre, title, page_number)",
                        [list_of_authors[author.get()], list_of_genres[genre.get()], title.get(), pages_int],
                        __file__)
                    msbox.showinfo('Success', 'Book has been added')

                except:
                    msbox.showerror('Error', 'Something went wrong')


window = Tk()
window.resizable(False, False)
window.title('Add new book')

labels = [
    "Title:",
    "Number of pages:",
    "Author:",
    "Genre:"
]

authors_query = "SELECT id, first_name, last_name FROM authors"
authors = Files.Database.select(authors_query)

genres_query = "SELECT id, name FROM genres"

genres = Files.Database.select(genres_query)

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

title = Entry(window, width=40)
title.focus()
title.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

number_of_pages = Entry(window, width=40)
number_of_pages.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

author = Combobox(window, width=37)
author.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

if authors:
    list_of_authors = dict(zip(
        [i[1] + ' ' + i[2] for i in authors],
        [i[0] for i in authors]
    ))

    list_of_authors_keys = list(list_of_authors.keys())

    author.config(state='readonly', values=list(list_of_authors_keys))

else:
    author.config(state='disabled')

genre = Combobox(window, width=37)
genre.grid(row=3, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

if genres:
    list_of_genres = dict(zip([i[1] for i in genres], [i[0] for i in genres]))

    list_of_genres_keys = list(list_of_genres.keys())

    genre.config(state='readonly', values=list_of_genres_keys)

else:
    genre.config(state='disabled')


insert_books_btn = Button(window, command=insert_book, text="Add book", bg="#D32F2F", fg="#fff")
insert_books_btn.grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert_book)

window.mainloop()
