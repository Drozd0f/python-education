"""This module contains custom descriptor"""


class IterableObject:
    """This class describes work descriptor for iterable object"""
    def __init__(self, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, args):
        for arg in args:
            if not isinstance(arg, (list, tuple)):
                raise TypeError(f'\'{type(arg)}\' object is not iterable')
        instance.__dict__[self._name] = args
