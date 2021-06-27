"""
Click is a Python package for creating command line interfaces in a composable way with as little code as necessary.
Import functions to use login.
"""
import click
from functions import *


"""
Indicate that the function is a click and therefore a command line interface function.
The option indicates that the user must enter a entry id.
"""
@click.command()
@click.option('-entry', required=True, type=int)
def delete_entries(entry):
    try:
        """
        Connecting to the database.
        """
        db = sqlite3.connect('../database.db')
        entry = entry
        """
        Declare statement.
        """
        statement = 'DELETE FROM MANAGER WHERE ID = ?'
        """ Cursor is to retrieve data, one row at a time. """
        cur = db.cursor()
        """
        Asking if the user really wants to delete the entry.
        """
        check = input("Are you sure you want to delete this entry (yes/no): ")
        """
        If the user input is yes.
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
    except ValueError as e:
        print("Error reading data from MySQL table", e)


"""
If this file is executed, run the login command and then the delete_entries.
"""
if __name__ == '__main__':
    login()
    delete_entries()
