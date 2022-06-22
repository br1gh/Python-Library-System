import re
from tkinter import *
from tkinter import messagebox as msbox
from tkcalendar import DateEntry
import Files.Database
import bcrypt


def main():
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

    logins_query = "SELECT login FROM readers"
    emails_query = "SELECT email FROM readers"

    logins = [''.join(i) for i in Files.Database.select(logins_query)]
    emails = [''.join(i) for i in Files.Database.select(emails_query)]

    for e, i in enumerate(labels):
        Label(
            window,
            text=labels[e],
        ).grid(row=e, column=0, sticky=W, padx=(20, 0), pady=(20, 0))

    def insert():
        values = [
            email.get(), login.get(), first_name.get(), last_name.get(),
            birth_date.get(), city.get(), street.get(), house_number.get(), phone.get()
        ]

        pw_values = [
            password.get(), confirm_password.get()
        ]

        if not all(values + pw_values):
            msbox.showerror('Error', 'All fields are required')

        elif len(pw_values[0]) < 5:
            msbox.showerror('Error', 'Password must be at least 5 characters')

        elif pw_values[0] != pw_values[1]:
            msbox.showerror('Error', 'Password does not match confirmation')

        elif len(values[1]) < 5:
            msbox.showerror('Error', 'Login must be at least 5 characters')

        elif values[1] in logins:
            msbox.showerror('Error', 'Login is taken')

        elif not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=values[0]):
            msbox.showerror('Error', 'Email address is incorrect')

        elif values[0] in emails:
            msbox.showerror('Error', 'Email is taken')

        else:
            try:
                pw = password.get().encode('utf-8')
                hashed_pw = str(bcrypt.hashpw(pw, bcrypt.gensalt()))[2:-1]
                Files.Database.insert(
                    "readers",
                    "(password, email, login, first_name, last_name, birth_date, city, street, house_number, phone)",
                    [hashed_pw] + values,
                    __file__)
                msbox.showinfo('Success', 'Account has been created')
            except:
                msbox.showerror('Error', 'Something went wrong')


    email = Entry(window, width=40)
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

    birth_date = DateEntry(window, state='readonly', width=37, date_pattern='YYYY-MM-DD')
    birth_date.grid(row=6, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    city = Entry(window, width=40)
    city.grid(row=7, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    street = Entry(window, width=40)
    street.grid(row=8, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    house_number = Entry(window, width=40)
    house_number.grid(row=9, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    phone = Entry(window, width=40)
    phone.grid(row=10, column=1, sticky=W, padx=(20, 20), pady=(20, 0), ipadx=5, ipady=5)

    register_btn = Button(window, command=insert, text="Register", bg="#388E3C", fg="#fff")
    register_btn.grid(row=11, column=0, columnspan=2, sticky=W+E, padx=(20, 20), pady=(20, 20), ipadx=5, ipady=5)
    window.bind('<Return>', insert)

    window.mainloop()
