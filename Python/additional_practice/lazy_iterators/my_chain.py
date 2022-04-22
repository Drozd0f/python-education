"""This module contains my chain lazy iterator"""
from itertools import chain

from additional_practice.lazy_iterators.descriptors import IterableObject


class MyChain:
    """This class describes work my chain lazy iterator"""
    _args = IterableObject('_args')

    def __init__(self, *args):
        self._args = args

    def _arguments(self):
        return (jdx for idx in self._args for jdx in idx)

    def __iter__(self):
        return self._arguments()


if __name__ == '__main__':
    ne_arr1 = [1, 2, 3]
    ne_arr2 = [5, 6, 7]
    assert list(MyChain(ne_arr1, ne_arr2)) == list(chain(ne_arr1, ne_arr2))
