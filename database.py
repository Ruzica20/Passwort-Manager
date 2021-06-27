"""
Import the sqlite3 module.
"""
import sqlite3


""" 
This function creates a sqlite database with a table named MANAGER.
This table contains the columns ID, USERNAME, TITLE, PASSWORD.
"""
def create_table():
	"""
	This connects to a database named database.db.
	If it does not exist it will create one.
	"""
	db = sqlite3.connect('database.db')

	""" This is the statement that sqlite uses to generate the table and the columns. """
	statement = '''CREATE TABLE if not exists MANAGER
	(ID INTEGER PRIMARY KEY AUTOINCREMENT,
	USERNAME TEXT NOT NULL,
	TITLE TEXT NOT NULL,
	PASSWORD TEXT NOT NULL
	);
	'''

	""" Cursor is to retrieve data, one row at a time. """
	cur = db.cursor()
	"""  Executes the statement. """
	cur.execute(statement)
	"""  Closes the database connection. """
	db.close()

#create_table()
