import Files.Database
import Files.GUI
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
controlTab = ttk.Notebook(root)

authors = Frame(controlTab)
books = Frame(controlTab)
borrows = Frame(controlTab)
copy = Frame(controlTab)
genres = Frame(controlTab)
readers = Frame(controlTab)

Files.GUI.authors_tab(authors, inserts["authors"])
Files.GUI.books_tab(books)
Files.GUI.borrows_tab(borrows)
Files.GUI.copy_tab(copy)
Files.GUI.genres_tab(genres, inserts["genres"])
Files.GUI.readers_tab(readers)

controlTab.add(authors, text='Authors')
controlTab.add(books, text='Books')
controlTab.add(borrows, text='Borrows')
controlTab.add(copy, text='Copies')
controlTab.add(genres, text='Genres')
controlTab.add(readers, text='Readers')


controlTab.pack()



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
