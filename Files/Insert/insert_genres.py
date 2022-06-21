from tkinter import *
from tkinter import messagebox as msbox
import Files.Database


def main():
    def insert_genre():
        if not genre.get():
            msbox.showerror('Error', "Genre is required")

        elif genre.get() in genres:
            msbox.showerror('Error', 'This genre already exists')

        else:
            try:
                Files.Database.insert(
                    "genres", "(name)", [genre.get()], __file__
                )
                msbox.showinfo('Success', 'Genre added')

            except:
                msbox.showerror('Error', 'Something went wrong')


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

    genre = Entry(window, width=40)
    genre.focus()
    genre.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    insert_genre_btn = Button(window, command=insert_genre, text="Add genre", bg="#D32F2F", fg="#fff")
    insert_genre_btn.grid(row=4, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    window.bind('<Return>', insert_genre)

    window.mainloop()
