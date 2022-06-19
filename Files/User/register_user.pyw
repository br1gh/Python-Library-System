import re
from tkinter import *
from tkinter import messagebox as msbox
from tkcalendar import DateEntry
import datetime
import Files.Database


window = Tk()
window.resizable(False, False)
window.title('Register')

labels = [
    "Email:",
    "Login:",
    "Password:",
    "Confirm password:",
    "First name:",
    "Last name:",
    "Birth date:",
    "City:",
    "Street:",
    "House number:",
    "Phone:",
]

query1 = "SELECT login FROM readers"
query2 = "SELECT email FROM readers"
logins = [''.join(i) for i in Files.Database.select(query1)]
emails = [''.join(i) for i in Files.Database.select(query2)]

for e, i in enumerate(labels):
    Label(
        window,
        text=labels[e],
    ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

def insert(event=None):
    if not all([email.get(), login.get(), password.get(), first_name.get(), last_name.get(), birth_date.get(), city.get(), street.get(), house_number.get(), phone.get()]):
        msbox.showinfo('Register Error', 'All fields are required')

    elif len(password.get()) < 5:
        msbox.showinfo('Register Error', 'Password must be at least 5 characters')

    elif password.get() != confirm_password.get():
        msbox.showinfo('Register Error', 'Password does not match confirmation')

    elif len(login.get()) < 5:
        msbox.showinfo('Register Error', 'Login must be at least 5 characters')

    elif login.get() in logins:
        msbox.showinfo('Register Error', 'Login is taken')

    elif not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email.get()):
        msbox.showinfo('Register Error', 'Email address is incorrect')

    elif email.get() in emails:
        msbox.showinfo('Register Error', 'Email is taken')

    else:
        Files.Database.insert(
            "readers", "(email, login, password, first_name, last_name, birth_date, city, street, house_number, phone)",
            [email.get(), login.get(), password.get(), first_name.get(), last_name.get(), birth_date.get(), city.get(), street.get(), house_number.get(), phone.get()],
            __file__)
        msbox.showinfo('Register Success', 'Account created')


email = Entry(window, width=40,)
email.focus()
email.grid(row=0, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

login = Entry(window, width=40)
login.grid(row=1, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

password = Entry(window, show='*', width=40)
password.grid(row=2, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

confirm_password = Entry(window, show='*', width=40)
confirm_password.grid(row=3, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

first_name = Entry(window, width=40)
first_name.grid(row=4, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

last_name = Entry(window, width=40)
last_name.grid(row=5, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

birth_date = DateEntry(window, width=37, date_pattern='YYYY-MM-DD')
birth_date.grid(row=6, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

city = Entry(window, width=40)
city.grid(row=7, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

street = Entry(window, width=40)
street.grid(row=8, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

house_number = Entry(window, width=40)
house_number.grid(row=9, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

phone = Entry(window, width=40)
phone.grid(row=10, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

button = Button(window, command=insert, text="Register", bg="#007bff", fg="#fff")
button.grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
window.bind('<Return>', insert)

window.mainloop()
