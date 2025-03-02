#!/usr/bin/python3
from add_0 import add  # "add_0" appears only once in this line

if __name__ == "__main__":  # Ensures script runs only when executed directly
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))  # Correct print formatting
