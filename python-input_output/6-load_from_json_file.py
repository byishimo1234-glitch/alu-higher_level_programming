#!/usr/bin/python3
"""
This module defines a function that creates an object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
    filename (str): The name of the JSON file to read from.

    Returns:
    object: The Python object represented by the JSON string in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

