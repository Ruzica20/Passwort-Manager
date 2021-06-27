"""
Import getpass for hidden password input, base64 to encode the input and the database to store everything there.
"""

import getpass
import base64
from database import *


def login():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('database.db')
    """ Cursor is to retrieve data, one row at a time. """
    cur = db.cursor()
    """
    Select the row in the database where the username is Master and put it in a result.
    """
    user_exits = cur.execute("SELECT * FROM MANAGER WHERE username='Master'")
    result = cur.fetchall()

    """
    If the users exists, asks for Master Password.
    """
    if result:
        """
        Asking for the Master Password using getpass.
        Getpass is a module which hides the input in the console.
        """
        masterpassword = getpass.getpass("Please provide your master password: ")
        """
        Hash the input to check if it is the same as it is in the database.
        """
        hashed = base64.b64encode(masterpassword.encode("utf-8"))
        cur.execute("SELECT PASSWORD FROM MANAGER WHERE username='Master'")
        """
        Fetch the first entry.
        """
        passcheck = cur.fetchone()
        inputpass = "(" + str(hashed) + ",)"
        """
        Check if passwords match, if not print "Wrong Password!" and exit.
        If the password is correct, print "Password Correct!".
        """
        if str(inputpass) != str(passcheck):
            print("Wrong Password!")
            exit(1)
        else:
            print("Password Correct!")
    else:
        """
        If the users does not exists, request a Master Password and create user.
        """
        statement = '''INSERT INTO MANAGER(USERNAME, TITLE, PASSWORD) VALUES (?, ?, ?)'''
        """
        Set username and title to Master.
        """
        username = "Master"
        title = "Master"
        """
        Asking to set Master Password using getpass.
        Getpass is a module which hides the input in the console.
        """
        masterpassword = getpass.getpass("Please set a Master Password: ")
        """
        Hash the input.
        """
        hashed = base64.b64encode(masterpassword.encode("utf-8"))
        """ Cursor is to retrieve data, one row at a time. """
        cur = db.cursor()
        """
        Execute the statement and commit it.
        """
        cur.execute(statement, (username, title, hashed))
        db.commit()
        """  Closes the database connection. """
        db.close()


def changeMasterPassword():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('database.db')
    """ Cursor is to retrieve data, one row at a time. """
    cur = db.cursor()
    """
    Asking to set a new Master Password using getpass.
    Getpass is a module which hides the input in the console.
    """
    new_masterpassword = getpass.getpass("Please set a new Master Password: ")
    """
    Hash the input.
    """
    hashed = base64.b64encode(new_masterpassword.encode("utf-8"))
    """
    Execute the statement and commit it.
    """
    cur.execute('''UPDATE MANAGER SET PASSWORD = ?, USERNAME = ?, TITLE = ? where id = 1''', (hashed, "Master", "Master"))
    db.commit()
    """  Closes the database connection. """
    db.close()
