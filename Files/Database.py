import sqlite3
import os.path
from pathlib import Path


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
            name varchar)''')

        cur.execute('''CREATE TABLE books(
            id INTEGER PRIMARY KEY autoincrement,
            id_author int,
            id_genre int,
            title varchar,
            page_number int)''')

        cur.execute('''CREATE TABLE copy(
            id INTEGER PRIMARY KEY autoincrement,
            id_book int,
            available boolean)''')

        cur.execute('''CREATE TABLE borrows(
             id INTEGER PRIMARY KEY autoincrement,
             id_reader int REFERENCES readers(id),
             id_copy int REFERENCES copy(id),
             borrow_date date,
             return_date date)''')

        con.commit()
        print('Database created')
        con.close()

    else:
        print('Database already exists')

def insert(arr, values):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    query = ("INSERT INTO " + arr[0] + arr[1] + " VALUES(" + str(values)[1:-1] + ")")
    cur.execute(query)
    con.commit()
    con.close()

def  select(query):
    con = sqlite3.connect(str(Path(__file__).parents[1]) + '\library.db')
    cur = con.cursor()
    data = cur.execute(query).fetchall()
    con.close()
    return data
