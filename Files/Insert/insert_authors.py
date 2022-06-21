from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox as msbox
import Files.Database


def main():
    def insert_author():
        if not first_name.get():
            msbox.showerror('Error', 'First name is required')

        elif not last_name.get():
            msbox.showerror('Error', 'Last name is required')
        else:
            try:
                Files.Database.insert(
                    "authors",
                    "(first_name, last_name, birth_date)",
                    [first_name.get(), last_name.get(), birth_date.get()],
                    __file__)

                msbox.showinfo('Success', 'Author has been added')

            except:
                msbox.showerror('Error', 'Something went wrong')

    window = Tk()
    window.resizable(False, False)
    window.title('Add new author')

    labels = [
        "First name:",
        "Last name:",
        "Birth date:"
    ]

    for e, i in enumerate(labels):
        Label(
            window,
            text=labels[e],
        ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

    first_name = Entry(window, width=40)
    first_name.focus()
    first_name.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    last_name = Entry(window, width=40)
    last_name.grid(row=1, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    birth_date = DateEntry(window, state='readonly', width=37, date_pattern='YYYY-MM-DD')
    birth_date.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    insert_authors_btn = Button(window, command=insert_author, text="Add", bg="#D32F2F", fg="#fff")
    insert_authors_btn.grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    window.bind('<Return>', insert_author)

    window.mainloop()
