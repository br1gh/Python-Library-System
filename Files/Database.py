import sqlite3


def create():
    con = sqlite3.connect('library.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE readers(
        id int primary key, 
        email varchar,
        login varchar,
        password varchar,
        first_name varchar,
        last_name varchar,
        birth_date date,
        city varchar,
        street varchar,
        house_number varchar,
        phone varchar)''')

    cur.execute('''CREATE TABLE authors(
        id int primary key, 
        first_name varchar,
        last_name varchar,
        birth_date date)''')

    cur.execute('''CREATE TABLE genres(
        id int primary key, 
        name varchar)''')

    cur.execute('''CREATE TABLE books(
        id int primary key, 
        id_author int,
        id_genre int,
        title varchar,
        page_number int)''')

    cur.execute('''CREATE TABLE copy(
        id int primary key, 
        id_book int,
        available boolean)''')

    cur.execute('''CREATE TABLE borrows(
         id int primary key, 
         id_reader int REFERENCES readers(id),
         id_copy int REFERENCES copy(id),
         borrow_date date,
         return_date date)''')

    con.commit()

    con.close()

def select():
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    data = cur.execute('select * from borrows').description
    print(data)