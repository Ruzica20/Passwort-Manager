"""
Import password to use the store_password, show_entries, delete_entries and retrieve_password functions.
Import masterPassword to use the login function.
"""
from password import *
from masterPassword import *

"""
Define all commands and assign them with functions.
"""
commands = {
    'create_entry': store_password,
    'entries': show_entries,
    'delete_entry': delete_entries,
    'get_password': retrieve_password,
    'change_master': changeMasterPassword,
    }


if __name__ == "__main__":
    """
    Calling the login function to check if the user is the Master or create a Master entry.
    """
    login()

    """
    Asking the user for a command.
    """
    while True:
        """
        Printing all commands, so the user can choose one.
        """
        print("Commands: create_entry, entries, delete_entry, get_password, change_master")
        command = input("Command: ").lower().split(" ")
        """
        Check if the command is available. If not, print "Command not found!"
        """
        if command[0] in commands:
            if len(command) > 1:
                commands[command[0]](command[1:])
            else:
                commands[command[0]]()
        else:
            print("Command not found!")
