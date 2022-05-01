"""This module contains recursive factorial implementation for exersice Algorithms - practice"""


def factorial(number) -> int:
    """This function return factorial of a number"""
    if number < 0:
        raise ValueError('factorial() not defined for negative values')
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)
