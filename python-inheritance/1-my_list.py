#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
MyList includes a method to print the list in sorted order.
"""

class MyList(list):
    """
    A subclass of list that provides an additional method
    to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        This method does not modify the original list.
        """
        print(sorted(self))

