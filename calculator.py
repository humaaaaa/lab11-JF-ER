"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError:
        return None
def logarithm(a, b):
    try:
        if b <= 0:
            raise ValueError
        return math.log(b, a)
    except ValueError:
        return None
def exponent(a, b): return a**b