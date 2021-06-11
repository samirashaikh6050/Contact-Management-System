from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as ms
import tkinter.messagebox as tkMessageBox
import sqlite3

with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()



class main:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.master.destroy()
            ms.showinfo("showinfo", "User Login Successful!!")
            DisplayForm()
        else:
            ms.showerror('Oops!', 'Incorrect Username or password')

    def new_user(self):
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()


    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=("Arial 1 6 italic", 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), fg="black", pady=5, padx=5 ).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15), bg="#ff9999").grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), fg="black", pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*', bg="#ff9999").grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), fg="black", bg="#ff0000", padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), fg="black", bg="#ff0000", padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), fg="black",  pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15), bg="#ff9999").grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), fg="black",pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*', bg="#ff9999").grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), fg="black", bg="#ff0000", padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), fg="black", bg="#ff0000", padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


def Database():
    global conn, cursor
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")


def DisplayForm():
    display_screen = Tk()
    display_screen.geometry("900x400")
    display_screen.title("Contact Management System")
    global tree
    global SEARCH
    global fname, lname, gender, address, contact
    SEARCH = StringVar(display_screen)
    fname = StringVar(display_screen)
    lname = StringVar(display_screen)
    gender = StringVar(display_screen)
    address = StringVar(display_screen)
    contact = StringVar(display_screen)

    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LFrom = Frame(display_screen, width="350", bg="#ff9999")
    LFrom.pack(side=LEFT, fill=Y)
    LeftViewForm = Frame(display_screen, width=500, bg="#ff8080")
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Contact Management System", font=('verdana', 18), width=600, bg="#ff0000")
    lbl_text.pack(fill=X)
    Label(LFrom, text="First Name  ", font=("Arial", 12), bg="#ff9999", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Last Name ", font=("Arial", 12), bg="#ff9999", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Arial", 12), bg="#ff9999", fg="white").pack(side=TOP)
    content = ['Male', 'Female']
    gender.set('Select Gender')
    gender_dropdown = OptionMenu(LFrom, gender, *content)
    gender_dropdown.pack(side=TOP, padx=10)

    Label(LFrom, text="Address ", font=("Arial", 12), bg="#ff9999", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12), bg="#ff9999", fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LFrom, text="Submit", font=("Arial", 10, "bold"), command=register, bg="#ff0000", fg="white").pack(side=TOP,
                                                                                                              padx=10,
                                                                                                              pady=5,
                                                                                                              fill=X)

    lbl_txtsearch = Label(LeftViewForm, text="Enter fname to Search", font=('verdana', 10), bg="#ff4d4d")
    lbl_txtsearch.pack()

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)

    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord, bg="#ff9999")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_view = Button(LeftViewForm, text="View All", command=DisplayData, bg="#ff9999")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_reset = Button(LeftViewForm, text="Reset", command=Reset, bg="#ff9999")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Delete", command=Delete, bg="#ff9999")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Update", command=Update, bg="#ff9999")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Student Id", "Name", "Contact", "Email", "Rollno", "Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('Name', text="FirstName", anchor=W)
    tree.heading('Contact', text="LastName", anchor=W)
    tree.heading('Email', text="Gender", anchor=W)
    tree.heading('Rollno', text="Address", anchor=W)
    tree.heading('Branch', text="Contact", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()



def Update():
    Database()

    fname1 = fname.get()
    lname1 = lname.get()
    gender1 = gender.get()
    address1 = address.get()
    contact1 = contact.get()

    if fname1 == '' or lname1 == '' or gender1 == '' or address1 == '' or contact1 == '':
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:

        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']

        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,GENDER=?,ADDRESS=?,CONTACT=? WHERE RID = ?',
                     (fname1, lname1, gender1, address1, contact1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message", "Updated successfully")

        Reset()

        DisplayData()
        conn.close()


def register():
    Database()

    fname1 = fname.get()
    lname1 = lname.get()
    gender1 = gender.get()
    address1 = address.get()
    contact1 = contact.get()

    if fname1 == '' or lname1 == '' or gender1 == '' or address1 == '' or contact1 == '':
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:

        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,GENDER,ADDRESS,CONTACT) \
              VALUES (?,?,?,?,?)', (fname1, lname1, gender1, address1, contact1));
        conn.commit()
        tkMessageBox.showinfo("Message", "Stored successfully")
        DisplayData()
        conn.close()


def Reset():

    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("Select Gender")
    address.set("")
    contact.set("")


def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def SearchRecord():
    Database()
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor = conn.execute("SELECT * FROM REGISTRATION WHERE FNAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()



def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor = conn.execute("SELECT * FROM REGISTRATION")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>", OnDoubleClick)
    cursor.close()
    conn.close()


def OnDoubleClick(self):
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    fname.set(selecteditem[1])
    lname.set(selecteditem[2])
    gender.set(selecteditem[3])
    address.set(selecteditem[4])
    contact.set(selecteditem[5])


if __name__ == '__main__':
    root = Tk()
    root.title('Login Form')
    main(root)
    root.mainloop()