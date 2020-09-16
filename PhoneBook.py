#  phonebook, simple with only two values, name and phone number
# must have sqlite3 to run it

import sqlite3 as lite

# setting empty phonebook for first time and if you run it again it will fetch all data from sqlite

phonebook = {}

con = lite.connect('Phonebook.db')
cur = con.cursor()

con.row_factory = lite.Row
cur.execute("SELECT * FROM PhoneBook")
rows = cur.fetchall()
phonebook.update(dict(rows))

cur.execute('DROP TABLE PhoneBook;')
choice = 0


# def for menu


def menu():
    print(" 1. Add a name")
    print(" 2. Search")
    print(" 3. Delete name")
    print(" 4. Show All")
    print(" 5. Edit")
    print(" 6. quit")


# def for adding name


def add_name():
    name = input("Name: ")
    phone = input("Phone number: ")
    phonebook[name] = phone


# search def


def search():
    search_name_or_number = input("Search: ")

    if search_name_or_number in phonebook.keys() or phonebook.values():
        for name, number in phonebook.items():
            print("Result: ", (name, number))
    else:
        print("No results")


# def to delete entry


def delete():
    _del = input("Enter name to delete: ")
    del phonebook[_del]


# def show phone book


def show_phonebook():
    print(phonebook)


# def for editing


def edit():
    _edit = input("Enter name to edit: ")
    new_number = input("Enter new number: ")
    phonebook[_edit] = new_number


menu()

# while loop with choices

while choice != "6":
    choice = input(" Choose an option: ")
    if choice == "1":
        add_name()
    if choice == "2":
        search()
    if choice == "3":
        delete()
    if choice == "4":
        show_phonebook()
    if choice == "5":
        edit()

# inserting values in phonebook and creating phonebook in sqlite for first time

cur.execute("CREATE TABLE IF NOT EXISTS PhoneBook(name, phone)")
list1 = list(phonebook.items())
for item in list1:
    cur.execute('INSERT INTO PhoneBook VALUES (?, ?)', item)

# commit and close connection

con.commit()
con.close()
print(phonebook)
