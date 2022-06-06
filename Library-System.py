import datetime
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
root.resizable(0, 0)
root.configure(background="#1c1c1c")
root.title('Library')

buttonClicked = False

full_date = datetime.datetime.now()
date = [int(full_date.strftime("%" + i)) for i in ["y", "m", "d"]]

def open_file(table, dir):
    print(exec(open("Files/" + dir + "/" + table + ".py").read()))

def generate_label(root, text, bg,col):
    Label(root, text=text, width=40, bg=bg, fg="#fff") \
        .grid(row=0, column=col, columnspan=2, sticky=W + E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_content = generate_label(root, "Show content", "#0D47A1", 0)
add_content = generate_label(root, "Add content", "#B71C1C", 2)
user = generate_label(root, "User", "#1B5E20", 4)

def generate_button(text, file, bg, fg, dir, row, col):
    return Button(root, text=text, command=lambda: open_file(file, dir), width=40, bg=bg, fg=fg)\
        .grid(row=row, column=col, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

show_authors_button = generate_button("Show authors", "show_authors", "#1976D2", "#fff", "Show", 1, 0)
show_books_button = generate_button("Show books", "show_books", "#1976D2", "#fff", "Show", 2, 0)
show_borrows_button = generate_button("Show borrows", "show_borrows", "#1976D2", "#fff", "Show", 3, 0)
show_copies_button = generate_button("Show copies", "show_copies", "#1976D2", "#fff", "Show", 4, 0)
show_genres_button = generate_button("Show genres", "show_genres", "#1976D2", "#fff", "Show", 5, 0)
show_readers_button = generate_button("Show readers", "show_readers", "#1976D2", "#fff", "Show", 6, 0)

insert_authors_button = generate_button("Add author", "insert_authors","#D32F2F", "#fff", "Insert",  1, 2)
insert_books_button = generate_button("Add book", "insert_books","#D32F2F", "#fff", "Insert",  2, 2)
insert_copies_button = generate_button("Add copy", "insert_copies","#D32F2F", "#fff", "Insert",  3, 2)
insert_genres_button = generate_button("Add genre", "insert_genre","#D32F2F", "#fff", "Insert",  4, 2)

register_button = generate_button("Register", "register_user","#388E3C", "#fff", "User",  1, 4)
login_button = generate_button("Login", "login_user","#388E3C", "#fff", "User",  2, 4)

#
# book_boorow_button = generate_button("Borrow book", "book_borrow", "Insert", 1, 4)
# book_return_button = generate_button("Reuturn book", "book_return", "Insert", 2, 4)

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
