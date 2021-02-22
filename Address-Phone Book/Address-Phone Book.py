#  App like many other address-phone book, call it what you want
#  You will need SQlite in order to run it

from tkinter import *
import sqlite3

# Setting root window with picture and background colour

root = Tk()
root.title("address-phone book")
root.geometry("500x500")
root.configure(bg='#EEF90B')
image = PhotoImage(file='python.png')
background_Label = Label(root, image=image)
background_Label.place(relwidth=0.3, relheight=0.3, relx=0.5, rely=1, anchor='s')

conn = sqlite3.connect('address_phone_book.db')
c = conn.cursor()

#  Create table addresses
c.execute(""" CREATE TABLE IF NOT EXISTS addresses(
    first_name text,
    last_name text,
    address text,
    email text,
    state text,
    phone integer
    )""")


#  create Submit function where entered data are being stored in SQlite


def submit():
    conn = sqlite3.connect('address_phone_book.db')
    c = conn.cursor()
    #  insert in table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :email, :state, :phone)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'email': email.get(),
                  'state': state.get(),
                  'phone': phone.get()
              })

    conn.commit()
    conn.close()

    # clearing boxes after submitting
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)
    state.delete(0, END)
    phone.delete(0, END)

#  edit def to store new data in ID we want to update
def edit1():
    conn = sqlite3.connect('address_phone_book.db')
    c = conn.cursor()

    record_id = deleteBox.get()

    c.execute("""UPDATE addresses SET
      first_name = :first,
      last_name = :last,
      address = :address,
      email = :email,
      state = :state,
      phone = :phone
      WHERE oid = :oid
      """,
              {
                  'first': f_name_edit.get(),
                  'last': l_name_edit.get(),
                  'address': address_edit.get(),
                  'email': email_edit.get(),
                  'state': state_edit.get(),
                  'phone': phone_edit.get(),
                  'oid': record_id
              })

    conn.commit()
    conn.close()

    edit.destroy()


# Update function with new window to get and change data in entry
def update():
    global edit
    edit = Tk()
    edit.title("Update a record")
    edit.geometry("400x400")

    conn = sqlite3.connect('address_phone_book.db')
    c = conn.cursor()

    record_id = deleteBox.get()
    c.execute('SELECT * FROM addresses WHERE oid = ' + record_id)
    records = c.fetchall()

    #  Create text boxes in new window

    global f_name_edit
    global l_name_edit
    global address_edit
    global email_edit
    global state_edit
    global phone_edit

    f_name_edit = Entry(edit, width=30)
    f_name_edit.grid(row=0, column=1)
    l_name_edit = Entry(edit, width=30)
    l_name_edit.grid(row=1, column=1)
    address_edit = Entry(edit, width=30)
    address_edit.grid(row=2, column=1)
    email_edit = Entry(edit, width=30)
    email_edit.grid(row=3, column=1)
    state_edit = Entry(edit, width=30)
    state_edit.grid(row=4, column=1)
    phone_edit = Entry(edit, width=30)
    phone_edit.grid(row=5, column=1)

    #  Create text box labels in new window

    f_name_label = Label(edit, text="First name")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(edit, text="Last name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(edit, text="Address")
    address_label.grid(row=2, column=0)
    email_label = Label(edit, text="Email")
    email_label.grid(row=3, column=0)
    state_label = Label(edit, text="State")
    state_label.grid(row=4, column=0)
    phone_label = Label(edit, text="Phone")
    phone_label.grid(row=5, column=0)

    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        email_edit.insert(0, record[3])
        state_edit.insert(0, record[4])
        phone_edit.insert(0, record[5])

    # save updated record button
    updatebtn = Button(edit, text="Save Updated Entry", command=edit1, bg='white')
    updatebtn.grid(row=6, column=0, columnspan=2, padx=15, pady=10, ipadx=125)


# delete a record
def delete():
    conn = sqlite3.connect('address_phone_book.db')
    c = conn.cursor()

    c.execute('DELETE FROM addresses WHERE oid= ' + deleteBox.get())

    conn.commit()
    conn.close()


#  create query function for showing data in book
def query():
    conn = sqlite3.connect('address_phone_book.db')
    c = conn.cursor()

    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()
    print_records = " "
    for record in records:
        print_records += str(record[0]) + "  " + str(record[1]) + "  " + str(record[2]) + "  " \
                         + str(record[3]) + "  " + str(record[4]) + "  " \
                         + str(record[5]) + "  " + str(record[6]) + "  " + "\n"

    querylbl = Label(root, text=print_records)
    querylbl.grid(row=12, column=0, columnspan=3)

    conn.commit()
    conn.close()


#  Create text boxes in root window

f_name = Entry(root, width=46)
f_name.grid(row=0, column=1)
l_name = Entry(root, width=46)
l_name.grid(row=1, column=1)
address = Entry(root, width=46)
address.grid(row=2, column=1)
email = Entry(root, width=46)
email.grid(row=3, column=1)
state = Entry(root, width=46)
state.grid(row=4, column=1)
phone = Entry(root, width=46)
phone.grid(row=5, column=1)
deleteBox = Entry(root, width=47)
deleteBox.grid(row=10, column=1)

#  Create text box labels in root window

f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last name", padx=1.8)
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address", padx=8)
address_label.grid(row=2, column=0)
email_label = Label(root, text="Email", padx=15)
email_label.grid(row=3, column=0)
state_label = Label(root, text="State", padx=17)
state_label.grid(row=4, column=0)
phone_label = Label(root, text="Phone", padx=13)
phone_label.grid(row=5, column=0)
deleteBox_label = Label(root, text="ID number", padx=10)
deleteBox_label.grid(row=10, column=0, padx=28)

#  Submit Button

submit_btn = Button(root, text="Submit data to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=3, padx=37, pady=7, ipadx=140)

#  query button
querybtn = Button(root, text="Show records", command=query)
querybtn.grid(row=7, column=0, columnspan=3, padx=8, pady=7, ipadx=169)

#  delete button
deletebtn = Button(root, text="DELETE   ID", command=delete, bg='red')
deletebtn.grid(row=9, column=0, columnspan=3, padx=9, pady=7, ipadx=176)

# Update button
updatebtn = Button(root, text="Update entry", command=update)
updatebtn.grid(row=11, column=0, columnspan=3, padx=5, pady=10, ipadx=171)

#  Commit changes and closing connection

conn.commit()

conn.close()

root.mainloop()
