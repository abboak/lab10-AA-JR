import math

# Repository: https://github.com/abboak/lab10-AA-JR
# Partner 1: Jack Reinhardt
# Partner 2: Abdulrahman Alkaelani

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm: base must be > 0 and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b


