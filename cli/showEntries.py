"""
Click is a Python package for creating command line interfaces in a composable way with as little code as necessary.
Import functions to use login.
"""
import click
from functions import *


"""
Indicate that the function is a click and therefore a command line interface function.
"""
@click.command()
def show_entries():
    """
    Connecting to the database.
    """
    db = sqlite3.connect('../database.db')
    """ Cursor is to retrieve data, one row at a time. """
    cur = db.cursor()
    """
    Execute the statement.
    """
    cur.execute("SELECT * FROM MANAGER")
    result = cur.fetchall()
    """
    Present the result(entries) in rows.
    """
    for row in result:
        print("Id = ", row[0], )
        print("Username = ", row[1])
        print("Title  = ", row[2])
        print("Password(Encoded)  = ", row[3], "\n")


"""
If this file is executed, run the login command and then the show_entries.
"""
if __name__ == '__main__':
    login()
    show_entries()
