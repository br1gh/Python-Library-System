from tkinter import *
from tkcalendar import DateEntry
import Files.Database
from tkinter import messagebox as msbox


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


def insert(event=None):
    if not first_name.get():
        msbox.showinfo('Error', 'First name field is required')
    if not last_name.get():
        msbox.showinfo('Error', 'Last name field is required')
    else:
        Files.Database.insert("authors", "(first_name, last_name, birth_date)", [first_name.get(), last_name.get(), birth_date.get()], __file__)
        msbox.showinfo('Success', 'Author has been added')

first_name = Entry(window, width=40)
first_name.focus()
first_name.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

last_name = Entry(window, width=40)
last_name.grid(row=1, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

birth_date = DateEntry(window, state='readonly', width=37, date_pattern='YYYY-MM-DD')
birth_date.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button1 = Button(window, command=insert, text="Add", bg="#007bff", fg="#fff").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert)

window.mainloop()
