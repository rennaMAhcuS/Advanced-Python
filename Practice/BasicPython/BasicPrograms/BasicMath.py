"""
            My Basic Math Functions
            -----------------------

My First Python Module, which contains the basic addition,
subtraction, multiplication and division functions:

add()
subtract()
multiply()
divide()
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error Dividing by Zero!", "Function Terminated!", sep="\n")
    else:
        return a / b
