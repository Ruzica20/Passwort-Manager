"""
Click is a Python package for creating command line interfaces in a composable way with as little code as necessary.
Import functions to use login.
"""

import click
from functions import *


"""
Indicate that the function is a click and therefore a command line interface function.
The option indicates that the user must enter a password.
"""
@click.command()
@click.option('-password')
def changeMasterPassword(password):
    """
    Connecting to the database.
    """
    db = sqlite3.connect('../database.db')
    """ Cursor is to retrieve data, one row at a time. """
    cur = db.cursor()
    """ Set the password. """
    new_masterpassword = password
    """
    Hash the input to check if it is the same as it is in the Database.
    """
    hashed = base64.b64encode(new_masterpassword.encode("utf-8"))
    """
    Execute the statement and commit it.
    """
    cur.execute('''UPDATE MANAGER SET PASSWORD = ?, USERNAME = ?, TITLE = ? where id = 1''', (hashed, "Master", "Master"))
    db.commit()
    """  Closes the database connection. """
    db.close()


"""
If this file is executed, run the login command and then the changeMasterPassword.
"""
if __name__ == '__main__':
    login()
    changeMasterPassword()
