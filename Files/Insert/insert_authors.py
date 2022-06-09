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

def insert(event=None):
    Files.Database.insert("authors", "(first_name, last_name, birth_date)", [first_name.get(), last_name.get(), birth_date.get()], __file__)

first_name = Entry(window)
first_name.focus()
first_name.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

last_name = Entry(window)
last_name.grid(row=1, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

birth_date = DateEntry(window)
birth_date.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button1 = Button(window, command=insert, text="Add", bg="#007bff", fg="#fff").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert)

window.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("Title")
# root.geometry('300x100')
#
# def new_label(event=None):
#     root = Tk()
#     root.title("Title")
#     root.geometry('300x100')
#     lbl1 = Label(root, text=txtE.get())
#     lbl1.pack()
#
#
# lbl1 = Label(root, text='Enter Your Name:')
# lbl1.pack()
# txtE = Entry(root)
# txtE.focus()
# txtE.pack()
#
# Button(root, text='Enter', command=new_label).pack()
# root.bind('<Return>', new_label)
# root.mainloop()
