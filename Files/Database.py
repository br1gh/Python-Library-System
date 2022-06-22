import sqlite3
import os.path


def create():
    if not os.path.exists('library.db'):
        con = sqlite3.connect('library.db')
        cur = con.cursor()

        cur.execute('''CREATE TABLE readers(
            id INTEGER PRIMARY KEY autoincrement,
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
            id INTEGER PRIMARY KEY autoincrement,
            first_name varchar,
            last_name varchar,
            birth_date date)''')

        cur.execute('''CREATE TABLE genres(
            id INTEGER PRIMARY KEY autoincrement,
            name varchar unique)''')

        cur.execute('''CREATE TABLE books(
            id INTEGER PRIMARY KEY autoincrement,
            id_author int,
            id_genre int,
            title varchar,
            page_number int)''')

        cur.execute('''CREATE TABLE copies(
            id INTEGER PRIMARY KEY autoincrement,
            id_book int,
            available boolean)''')

        cur.execute('''CREATE TABLE borrows(
             id INTEGER PRIMARY KEY autoincrement,
             id_reader int REFERENCES readers(id),
             id_copy int REFERENCES copy(id),
             borrow_date smalldatetime,
             return_date smalldatetime)''')

        con.commit()
        con.close()
        return 1
    return 0


def insert(table, columns, values):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    query = ("INSERT INTO " + table + columns + " VALUES(" + str(values)[1:-1] + ")")
    cur.execute(query)
    con.commit()
    con.close()


def update_copy_available(id, value):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    query = ("UPDATE copies SET available = " + str(value) + " WHERE id = " + str(id))
    cur.execute(query)
    con.commit()
    con.close()


def update_return_date(id, date):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    query = ("UPDATE borrows SET return_date = '" + str(date) + "' WHERE id = " + str(id))
    cur.execute(query)
    con.commit()
    con.close()


def select(query):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    data = cur.execute(query).fetchall()
    con.close()
    return data
