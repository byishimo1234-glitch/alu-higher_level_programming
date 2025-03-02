#!/usr/bin/python3
from add_0 import add  # Import add function (only one mention of 'add_0')

if __name__ == "__main__":  # Ensures the script runs only when executed directly
    a = 1  # Define a on a separate line
    b = 2  # Define b on another line

    print("{} + {} = {}".format(a, b, add(a, b)))  # Print formatted output
