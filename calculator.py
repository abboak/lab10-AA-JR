"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example


import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b

