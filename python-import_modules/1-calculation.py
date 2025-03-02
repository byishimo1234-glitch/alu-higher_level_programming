#!/usr/bin/python3

# Define the functions from calculator_1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# Main program logic
if __name__ == "__main__":
    a = 10
    b = 5

    # Perform calculations and store results in a list
    results = [
        "{} + {} = {}".format(a, b, add(a, b)),
        "{} - {} = {}".format(a, b, sub(a, b)),
        "{} * {} = {}".format(a, b, mul(a, b)),
        "{} / {} = {}".format(a, b, div(a, b))
    ]

    # Print all results using a single print function
    print("\n".join(results))
