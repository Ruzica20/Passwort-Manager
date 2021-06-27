"""
Click is a Python package for creating command line interfaces in a composable way with as little code as necessary.
Import functions to use login.
"""
import click
import secrets
import string
from functions import *


"""
Indicate that the function is a click and therefore a command line interface function.
The option indicates that the user must enter a username and title.
"""
@click.command()
@click.option('-username', required=True)
@click.option('-title', required=True)
def store_password(username, title):
    """
    Connecting to the database.
    """
    db = sqlite3.connect('../database.db')
    statement = '''INSERT INTO MANAGER(USERNAME, TITLE, PASSWORD) VALUES (?,?,?)'''
    # USERNAME
    username = username
    # TITLE
    title = title
    # PASSWORD
    password = ""

    """
    The size is the length of the password.
    """
    size = 12
    chars = string.digits + string.ascii_letters + string.punctuation
    password += ''.join(secrets.choice(chars) for l in range(size))
    """
    Hash the input to check if it is the same as it is in the database.
    """
    hashed = password.encode("UTF-8")
    """ Cursor is to retrieve data, one row at a time. """
    cur = db.cursor()
    """
    Execute the statement and commit it.
    """
    cur.execute(statement, (username, title, hashed))
    db.commit()
    """  Closes the database connection. """
    db.close()
    print(f'Password for {title} successfully created!')


"""
If this file is executed, run the login command and then the store_password.
"""
if __name__ == '__main__':
    login()
    store_password()
