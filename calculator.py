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




