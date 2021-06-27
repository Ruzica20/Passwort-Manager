"""
Import getpass for hidden password input, base64 to encode the input and the database to store everything there.
"""

import getpass
import sys
sys.path.append('../')
from database import *
import base64


def login():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('../database.db')
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
        """
        Check if passwords match, if not print "Wrong Password!" and exit.
        If the password is correct, print "Password Correct!".
        """
        inputpass = "(" + str(hashed) + ",)"
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


"""
This function checks whether the user's input is an integer or something else such as text, point numbers, etc..
"""


def validator(message):
    """
    Starts a infinity loop.
    """
    while True:
        """
        Check if user input is an integer.
        """
        try:
            userInput = int(input(message))
        except ValueError:
            """
            If user input is not an integer then print an error and continue the loop.
            """
            print("Not an integer! Try again.")
            continue
        else:
            """
            If user input is an integer break the loop.
            """
            return userInput
            break
