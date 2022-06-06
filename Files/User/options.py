import datetime
from tkinter import *
from tkinter import ttk
import Files.Database

options = Tk()
options.resizable(0, 0)
options.configure(background="#1c1c1c")
options.title('Options')

def open_file(window, file):
    window.destroy()
    print(exec(open(file + ".py").read()))


def generate_button(window, text, file, bg, fg, row):
    return Button(window, text=text, command=lambda: open_file(options, file), width=40, bg=bg, fg=fg)\
        .grid(row=row, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

# show_authors_button = generate_button(window,"Borrow book", "borrow", "#1976D2", "#fff", 0)
# show_books_button = generate_button(window,"Return book", "return", "#1976D2", "#fff", 1)
show_borrows_button = generate_button(options, "Show borrowed books", "user_borrows", "#1976D2", "#fff", 2)

options.mainloop()
