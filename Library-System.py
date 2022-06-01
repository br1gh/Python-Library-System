from tkinter import *
from tkinter import ttk

inserts = {
    "readers": ["readers",
                "(email, login, password, first_name, last_name, birth_date, city, street, house_number, phone)"],
    "authors": ["authors", "(first_name, last_name, birth_date)"],
    "genres": ["genres", "(name)"],
    "books": ["books", "(id_author, id_genre, title, page_number)"],
    "copy": ["copy", "(id_book, available)"],
    "borrows": ["borrows", "(id_reader, id_copy, borrow_date, return_date)"]
}

root = Tk()
root.title('Library')
root['bg'] = '#fff'

buttonClicked = False

def show(table):
    print(exec(open("Files/Show/show_" + table + ".py").read()))


show_authors = ttk.Button(root, text="Authors", command=lambda: show("authors"), width=20)
show_authors.pack()

show_books = ttk.Button(root, text="Books", command=lambda: show("books"), width=20)
show_books.pack()

show_borrows = ttk.Button(root, text="Borrows", command=lambda: show("borrows"), width=20)
show_borrows.pack()

show_copies = ttk.Button(root, text="Copies", command=lambda: show("copies"), width=20)
show_copies.pack()

show_genres = ttk.Button(root, text="Genres", command=lambda: show("genres"), width=20)
show_genres.pack()

show_readers = ttk.Button(root, text="Readers", command=lambda: show("readers"), width=20)
show_readers.pack()



# controlTab.pack()

root.mainloop()

# Files.Database.insert(inserts["authors"], ['Krzysztof', 'Krawczyk', '2022-01-01'])
# Files.Database.insert(inserts["books"], [1,1,'title1',1])
# Files.Database.insert(inserts["borrows"], [1,1,'2022-01-01', '2022-01-02'])
# Files.Database.insert(inserts["copy"], [1,0])
# Files.Database.insert(inserts["genres"], ['genre1'])
# Files.Database.insert(inserts["readers"], ['ok1@ok.pl', 'test1', 'password1', 'first1', 'last1', '2022-01-20', 'city', 'street', 'number', 'phone'])

# Files.Database.create()
#
# Files.Database.select()
