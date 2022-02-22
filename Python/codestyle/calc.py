"""This module contains a calculator class"""


class Calculator:
    """This class performs calculator tasks"""
    @staticmethod
    def addition(first_arg: (int, float), last_arg: (int, float)):
        """This function returns the sum of two numeric arguments"""
        if isinstance(first_arg, (int, float)) and isinstance(last_arg, (int, float)):
            return first_arg + last_arg
        return TypeError('Impossible addition, one or both arguments are not numeric')

    @staticmethod
    def difference(first_arg: (int, float), last_arg: (int, float)):
        """This function returns the difference of two numeric arguments"""
        if isinstance(first_arg, (int, float)) and isinstance(last_arg, (int, float)):
            return first_arg - last_arg
        return TypeError('Impossible difference, one or both arguments are not numeric')

    @staticmethod
    def multiplication(first_arg: (int, float), last_arg: (int, float)):
        """This function returns the multiplication of two numeric arguments"""
        if isinstance(first_arg, (int, float)) and isinstance(last_arg, (int, float)):
            return first_arg * last_arg
        return TypeError('Impossible multiplication, one or both arguments are not numeric')

    @staticmethod
    def division(first_arg: (int, float), last_arg: (int, float)):
        """This function returns the division of two numeric arguments"""
        if isinstance(first_arg, (int, float)) and isinstance(last_arg, (int, float)):
            try:
                return first_arg / last_arg
            except ZeroDivisionError as exception:
                return exception
        return TypeError('Impossible division, one or both arguments are not numeric')
