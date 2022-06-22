from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as msbox
import Files.Database


def main():
    def insert_copies():
        if not books or not book.get():
            msbox.showerror('Error', "Book is required! Add the new one if field is disabled")

        else:
            if not amount.get():
                msbox.showerror('Error', "Amount is required")

            else:
                try:
                    amount_int = int(amount.get())

                except:
                    msbox.showerror('Error', 'Amount must be an integer')

                else:
                    if amount_int < 1:
                        msbox.showerror('Error', 'Amount must greater than 0')

                    else:
                        try:
                            for _ in range(amount_int):
                                Files.Database.insert(
                                    "copies", "(id_book, available)",
                                    [list_of_books[book.get()], 1],
                                )
                            msbox.showinfo('Success', 'Added ' + str(amount_int) + ' copies of this book')

                        except:
                            msbox.showerror('Error', 'Something went wrong')


    window = Tk()
    window.resizable(False, False)
    window.title('Add new copies')


    labels = [
        "Book:",
        "Amount:",
    ]

    books_query = "SELECT books.id, title, first_name, last_name FROM books " \
                  "INNER JOIN authors ON books.id_author = authors.id"

    books = Files.Database.select(books_query)

    for e, i in enumerate(labels):
        Label(
            window,
            text=labels[e],
        ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

    amount = Entry(window, width=40)
    amount.focus()
    amount.grid(row=1, column=1, padx=(20, 20), pady=(20,0), ipadx=5, ipady=5)

    book = Combobox(window, width=37)
    book.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    if books:
        list_of_books = dict(zip([i[1] + " by " + i[2] + " " + i[3] for i in books], [i[0] for i in books]))
        list_of_books_keys = list(list_of_books.keys())

        book.config(state='readonly', values=list_of_books_keys)

    else:
        book.config(state='disabled')

    insert_copies_btn = Button(window, command=insert_copies, text="Add copies", bg="#D32F2F", fg="#fff")
    insert_copies_btn.grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    window.bind('<Return>', insert_copies)

    window.mainloop()
