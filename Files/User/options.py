import datetime
from tkinter import *
from tkinter import ttk
import Files.Database

options = Tk()
options.resizable(0, 0)
options.configure(background="#1c1c1c")
options.title('Options')

def generate_button(window, text, file, bg, fg, row):
    def filename():
        return "Files/User/" + file + ".py" if "Library-System.py" in __file__ else file + ".py"

    return Button(window, text=text, command=lambda: exec(open(filename()).read()), width=40, bg=bg, fg=fg)\
        .grid(row=row, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_authors_button = generate_button(options, "Borrow book", "borrow", "#1976D2", "#fff", 0)
show_books_button = generate_button(options, "Return book", "return", "#1976D2", "#fff", 1)
show_borrows_button = generate_button(options, "Show borrowed books", "user_borrows", "#1976D2", "#fff", 2)

options.mainloop()
