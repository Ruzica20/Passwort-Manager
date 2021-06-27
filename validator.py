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
