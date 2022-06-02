from tkinter import *
from tkinter import ttk
import Files.Database
#
inserts = {
    "readers": ["readers",
                "(email, login, password, first_name, last_name, birth_date, city, street, house_number, phone)"],
    "authors": ["authors", "(first_name, last_name, birth_date)"],
    "genres": ["genres", "(name)"],
    "books": ["books", "(id_author, id_genre, title, page_number)"],
    "copy": ["copy", "(id_book, available)"],
    "borrows": ["borrows", "(id_reader, id_copy, borrow_date, return_date)"]
}


Files.Database.create()

root = Tk()
root.title('Library')
root['bg'] = '#fff'

buttonClicked = False

def show(table):
    print(exec(open("Files/Show/show_" + table + ".py").read()))


label = Label(root,text="Select table to show:", width=40,  height=2)
label.pack()


show_authors = ttk.Button(root, text="Authors", command=lambda: show("authors"), width=40)
show_authors.pack()

show_books = ttk.Button(root, text="Books", command=lambda: show("books"), width=40)
show_books.pack()

show_borrows = ttk.Button(root, text="Borrows", command=lambda: show("borrows"), width=40)
show_borrows.pack()

show_copies = ttk.Button(root, text="Copies", command=lambda: show("copies"), width=40)
show_copies.pack()

show_genres = ttk.Button(root, text="Genres", command=lambda: show("genres"), width=40)
show_genres.pack()

show_readers = ttk.Button(root, text="Readers", command=lambda: show("readers"), width=40)
show_readers.pack()

root.mainloop()

# Files.Database.insert(inserts["authors"], ['Krzysztof1', 'Krawczyk1', '2022-01-01'])
# Files.Database.insert(inserts["authors"], ['Krzysztof2', 'Krawczyk2', '2022-01-02'])
# Files.Database.insert(inserts["authors"], ['Krzysztof3', 'Krawczyk3', '2022-01-03'])
# Files.Database.insert(inserts["authors"], ['Krzysztof4', 'Krawczyk4', '2022-01-04'])
# Files.Database.insert(inserts["authors"], ['Krzysztof5', 'Krawczyk5', '2022-01-05'])
# Files.Database.insert(inserts["authors"], ['Krzysztof6', 'Krawczyk6', '2022-01-06'])
# Files.Database.insert(inserts["authors"], ['Krzysztof7', 'Krawczyk7', '2022-01-07'])
# Files.Database.insert(inserts["authors"], ['Krzysztof8', 'Krawczyk8', '2022-01-08'])
# Files.Database.insert(inserts["authors"], ['Krzysztof8', 'Krawczyk9', '2022-01-09'])
# Files.Database.insert(inserts["authors"], ['Krzysztof8', 'Krawczyk10', '2022-01-10'])
#
#
#
# Files.Database.insert(inserts["books"], [1,1,'title',1])
# Files.Database.insert(inserts["books"], [2,2,'title',2])
# Files.Database.insert(inserts["books"], [3,3,'title',3])
# Files.Database.insert(inserts["books"], [4,4,'title',4])
# Files.Database.insert(inserts["books"], [5,5,'title',5])
# Files.Database.insert(inserts["books"], [6,6,'title',6])
# Files.Database.insert(inserts["books"], [7,7,'title',7])
# Files.Database.insert(inserts["books"], [8,8,'title',8])
# Files.Database.insert(inserts["books"], [9,9,'title',9])
# Files.Database.insert(inserts["books"], [10,10,'title',10])
#
#
# Files.Database.insert(inserts["borrows"], [1,1,'2022-01-01', '2022-01-11'])
# Files.Database.insert(inserts["borrows"], [2,2,'2022-01-02', '2022-01-12'])
# Files.Database.insert(inserts["borrows"], [3,3,'2022-01-03', '2022-01-13'])
# Files.Database.insert(inserts["borrows"], [4,4,'2022-01-04', '2022-01-14'])
# Files.Database.insert(inserts["borrows"], [5,5,'2022-01-05', '2022-01-15'])
# Files.Database.insert(inserts["borrows"], [6,6,'2022-01-06', '2022-01-16'])
# Files.Database.insert(inserts["borrows"], [7,7,'2022-01-07', '2022-01-17'])
# Files.Database.insert(inserts["borrows"], [8,8,'2022-01-08', '2022-01-18'])
# Files.Database.insert(inserts["borrows"], [9,9,'2022-01-09', '2022-01-19'])
# Files.Database.insert(inserts["borrows"], [10,10,'2022-01-10', '2022-01-20'])
#
#
#
#
# Files.Database.insert(inserts["copy"], [1,0])
# Files.Database.insert(inserts["copy"], [2,1])
# Files.Database.insert(inserts["copy"], [3,0])
# Files.Database.insert(inserts["copy"], [4,1])
# Files.Database.insert(inserts["copy"], [5,0])
# Files.Database.insert(inserts["copy"], [6,1])
# Files.Database.insert(inserts["copy"], [7,0])
# Files.Database.insert(inserts["copy"], [8,1])
# Files.Database.insert(inserts["copy"], [9,0])
# Files.Database.insert(inserts["copy"], [10,1])
#
#
#
# Files.Database.insert(inserts["genres"], ['genre1'])
# Files.Database.insert(inserts["genres"], ['genre2'])
# Files.Database.insert(inserts["genres"], ['genre3'])
# Files.Database.insert(inserts["genres"], ['genre4'])
# Files.Database.insert(inserts["genres"], ['genre5'])
# Files.Database.insert(inserts["genres"], ['genre6'])
# Files.Database.insert(inserts["genres"], ['genre7'])
# Files.Database.insert(inserts["genres"], ['genre8'])
# Files.Database.insert(inserts["genres"], ['genre9'])
# Files.Database.insert(inserts["genres"], ['genre10'])
#
#
# Files.Database.insert(inserts["readers"], ['ok1@ok.pl', 'test1', 'password1', 'first1', 'last1', '2000-01-01', 'city1', 'street1', 'number1', 'phone1'])
# Files.Database.insert(inserts["readers"], ['ok2@ok.pl', 'test2', 'password2', 'first2', 'last2', '2000-01-02', 'city2', 'street2', 'number2', 'phone2'])
# Files.Database.insert(inserts["readers"], ['ok3@ok.pl', 'test3', 'password3', 'first3', 'last3', '2000-01-03', 'city3', 'street3', 'number3', 'phone3'])
# Files.Database.insert(inserts["readers"], ['ok4@ok.pl', 'test4', 'password4', 'first4', 'last4', '2000-01-04', 'city4', 'street4', 'number4', 'phone4'])
# Files.Database.insert(inserts["readers"], ['ok5@ok.pl', 'test5', 'password5', 'first5', 'last5', '2000-01-05', 'city5', 'street5', 'number5', 'phone5'])
# Files.Database.insert(inserts["readers"], ['ok6@ok.pl', 'test6', 'password6', 'first6', 'last6', '2000-01-06', 'city6', 'street6', 'number6', 'phone6'])
# Files.Database.insert(inserts["readers"], ['ok7@ok.pl', 'test7', 'password7', 'first7', 'last7', '2000-01-07', 'city7', 'street7', 'number7', 'phone7'])
# Files.Database.insert(inserts["readers"], ['ok8@ok.pl', 'test8', 'password8', 'first8', 'last8', '2000-01-08', 'city8', 'street8', 'number8', 'phone8'])
# Files.Database.insert(inserts["readers"], ['ok9@ok.pl', 'test9', 'password9', 'first9', 'last9', '2000-01-09', 'city9', 'street9', 'number9', 'phone9'])
# Files.Database.insert(inserts["readers"], ['ok10@ok.pl', 'test10', 'password10', 'first10', 'last10', '2000-01-10', 'city10', 'street10', 'number10', 'phone10'])


# Files.Database.insert(inserts["readers"], ['ok1@ok.pl', 'test1', 'password1', 'first1', 'last1', '2022-01-20', 'city', 'street', 'number', 'phone'])

# # Files.Database.create()
# #
# # Files.Database.select()
