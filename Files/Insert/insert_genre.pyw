from tkinter import *
from tkinter import messagebox as msbox
import Files.Database

window = Tk()
window.resizable(False, False)
window.title('Add new genre')

labels = [
    "Genre:",
]

query = "SELECT name FROM genres"
genres = [''.join(i) for i in Files.Database.select(query)]

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))


def insert(event=None):
    if genre.get() in genres:
        msbox.showinfo('Error', 'This genre already exists')
    else:
        Files.Database.insert("genres", "(name)", [genre.get()], __file__)
        msbox.showinfo('Success', 'Genre added')


genre = Entry(window, width=40)
genre.focus()
genre.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button1 = Button(window, command=insert, text="Add", bg="#007bff", fg="#fff").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert)

window.mainloop()
