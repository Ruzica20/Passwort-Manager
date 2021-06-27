"""
Import sqlite3, secrets, string, time, pyperclip, base64, validator.
Time to wait after a Thread.
Pyperclip module for copying to clipboard.
Base64 for encoding.
Validator to validate integer input.
"""
import sqlite3
import secrets
import string
import time
import pyperclip
import base64
from validator import *


def store_password():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('database.db')
    """
    SQL statement to insert the entry data.
    """
    statement = '''INSERT INTO MANAGER(USERNAME, TITLE, PASSWORD) VALUES (?,?,?)'''
    """
    Username input.
    """
    username = str(input("Your username: "))
    # TITLE
    """
    Title input.
    """
    title = str(input("Title: "))
    # PASSWORD
    password = ""

    """
    Validating options.
    """
    option = validator("Option: (1) Generate random password | (2) Customize password: ")

    """
    If option 1.
    """
    if option == 1:
        """
        Asking for password length and validate.
        """
        size = validator("Password length: ")
        """
        Declaring that the password contains chars, digits and punctuation.
        """
        chars = string.digits + string.ascii_letters + string.punctuation
        password += ''.join(secrets.choice(chars) for l in range(size))
        """
        Hash the input.
        """
        hashed = base64.b64encode(password.encode("utf-8"))
        cur = db.cursor()
        """
        Execute the statement and commit it.
        """
        cur.execute(statement, (username, title, hashed))
        db.commit()
        """  Closes the database connection. """
        db.close()
        """
        Print that the entry successfully was created.
        """
        print(f'Password for {title} succsessfully created!')
    elif option == 2:
        """
        Asking for password length and validating.
        """
        size = validator("Password length: ")
        """
        Asking if what type of chars the password should contain and validate.
        """
        chars = validator("(1) Upper | (2) Lower | (3) Both: ")
        if chars == 1:
            chars = string.ascii_uppercase
        elif chars == 2:
            chars = string.ascii_lowercase
        elif chars == 3:
            chars = string.ascii_letters
        else:
            print("Not a valid option!")
        """
        Asking if the password should contain special characters or not and validate.
        """
        special = validator("Special characters? (1) Yes | (2) No: ")
        if special == 1:
            special = string.punctuation
        else:
            special = None
        """
        Asking if the password should contain digits and validate.
        """
        digits = validator("Digits? (1) Yes | (2) No: ")
        if digits == 1:
            digits = string.digits
        else:
            digits = None
        combine = str(chars) + str(special) + str(digits)
        """
        Hash the input.
        """
        password += ''.join(secrets.choice(combine) for l in range(size))
        hashed = base64.b64encode(password.encode("utf-8"))
        cur = db.cursor()
        """
        Execute the statement and commit it.
        """
        cur.execute(statement, (username, title, hashed))
        db.commit()
        """  Closes the database connection. """
        db.close()
        """
        Print that the entry successfully was created.
        """
        print(f'Password for {title} succsessfully created!')
    else:
        print("Not a valid option")


def show_entries():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('database.db')
    cur = db.cursor()
    """
    Select everything from MANAGER(Table) and put it in results.
    """
    cur.execute("SELECT * FROM MANAGER")
    result = cur.fetchall()
    """
    Show the results in a row.
    """
    for row in result:
        print("Id = ", row[0], )
        print("Username = ", row[1])
        print("Title  = ", row[2])
        print("Password(Encoded)  = ", row[3], "\n")


def retrieve_password():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('database.db')
    """
    Asking for the entry ID and validate.
    """
    entry = validator("Which entry you want the password from: ")
    """
    Declare statement.
    """
    statement = 'SELECT password FROM MANAGER WHERE ID = ?'
    cur = db.cursor()
    """
    Execute the statement.
    """
    items = cur.execute(statement, (entry,))
    password_list = [i for i in items]
    """
    Decoding the password.
    """
    password = base64.b64decode(password_list[-1][0]).decode("utf-8")
    """
    Copy the decoded password into the clipboard.
    """
    pyperclip.copy(str(password))
    """
    Wait 30 seconds and clear the clipboard.
    """
    time.sleep(30)
    pyperclip.copy("")

    print("Password copied to clipboard!")


def delete_entries():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('database.db')
    """
    Asking for the entry ID and validate.
    """
    entry = validator("Which entry you want to delete: ")
    """
    Declare statement.
    """
    statement = 'DELETE FROM MANAGER WHERE ID = ?'
    cur = db.cursor()
    """
    Asking if the user really wants to delete the entry.
    """
    check = input("Are you sure you want to delete this entry (yes/no): ")
    """
    If the user input is yes
    """
    if check == "yes":
        """
        Execute the statement and commit it.
        """
        cur.execute(statement, (entry,))
        db.commit()
        """  Closes the database connection. """
        db.close()
        print("Entry " + str(entry) + " deleted!")
    else:
        print("Nothing deleted!")
