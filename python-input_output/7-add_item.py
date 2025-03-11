#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file named add_item.json.
It checks for the existence of the file and handles different cases based on the file's content.
"""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    """
    Main function that adds command-line arguments to a list and saves them to a file.

    If the file exists, it loads the current list and appends new arguments.
    If the file doesn't exist, it creates the file and initializes the list with the arguments.
    """
    try:
        # Try to load existing data from the file
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If file doesn't exist, create an empty list
        items = []

    # Add the arguments (excluding the script name) to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, 'add_item.json')


if __name__ == "__main__":
    main()

