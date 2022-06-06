from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
import Files.Database

window = Tk()
window.resizable(0, 0)
window.title('Add new author')
window.configure(background="#1c1c1c")

labels = [
    "First name:",
    "Last name:",
    "Birth date:"
]

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
        bg='#1c1c1c',
        fg="#fff",
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]

def generate_entry(root, row, show = ""):
    print(Entry(root, show=show, bg='#282828', fg="#eee", insertbackground="#eee", width=40).grid(row=row, column=1, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5))

first_name = generate_entry(window, 0)
last_name = generate_entry(window, 1)

birth_date = DateEntry(window, width=37, year=date[0], month=date[1], day=date[2], background='#bbb', foreground='#fff',
                borderwidth=2).grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button = Button(window, text="Add", bg="#007bff", fg="#fff").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)

window.mainloop()
