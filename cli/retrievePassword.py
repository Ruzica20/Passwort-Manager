"""
Click is a Python package for creating command line interfaces in a composable way with as little code as necessary.
Import functions to use login.
Import base64 to encode the input.
"""
from functions import *
import click
import sqlite3
import pyperclip
import base64


"""
Indicate that the function is a click and therefore a command line interface function.
The option indicates that the user must enter a entry id.
"""
@click.command()
@click.option('-entry', required=True, type=int)
def retrieve_password(entry):
    """
    Connecting to the database.
    """
    db = sqlite3.connect('../database.db')
    entry = entry
    """
    Declare statement.
    """
    statement = 'SELECT password FROM MANAGER WHERE ID = ?'
    """ Cursor is to retrieve data, one row at a time. """
    cur = db.cursor()
    """
    Execute the statement.
    """
    items = cur.execute(statement, (entry,))
    password_list = [i for i in items]
    """
    Decode the password.
    """
    password = base64.b64decode(password_list[-1][0]).decode("utf-8")
    """
    Copy the password into the clipboard.
    """
    pyperclip.copy(str(password))

    print("Password copied to clipboard!")


"""
If this file is executed, run the login command and then the retrieve_password.
"""
if __name__ == '__main__':
    login()
    retrieve_password()
