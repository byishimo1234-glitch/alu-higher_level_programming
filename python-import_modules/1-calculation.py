#!/usr/bin/python3

# Define the fake functions
def add(a, b):
    return a - b  # Fake add() behaves like sub()


def sub(a, b):
    return a + b  # Fake sub() behaves like add()


def mul(a, b):
    return a / b  # Fake mul() behaves like div()


def div(a, b):
    return a * b  # Fake div() behaves like mul()


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
