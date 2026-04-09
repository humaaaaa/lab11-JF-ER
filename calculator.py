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
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")

def log(a, b):
    try:
        math.log(a,b)
    except ValueError:
        return None

def exp(a, b):
    return math.pow(a,b)



def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def logarithm(a, b):
    try:
        if b <= 0:
            raise ValueError
        return math.log(b, a)
    except ValueError:
        return None
def exponent(a, b): return a**b