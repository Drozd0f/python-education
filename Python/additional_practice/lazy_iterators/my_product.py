"""This module contains my product lazy iterator"""
from itertools import product

from additional_practice.lazy_iterators.descriptors import IterableObject


class MyProduct:
    """This class describes work my product lazy iterator"""
    _args = IterableObject('_args')

    def __init__(self, *args, repeat: int = 1):
        self._args = args
        if not isinstance(repeat, int):
            raise TypeError
        self._repeat = repeat

    def _gen_pools(self):
        pools = tuple(pool for pool in self._args) * self._repeat
        return pools

    def _gen_combination(self):
        comb = [[]]
        for pool in self._gen_pools():
            comb = [x + [y] for x in comb for y in pool]
        return comb

    def _arguments(self):
        return (tuple(comb) for comb in self._gen_combination())

    def __iter__(self):
        return self._arguments()


if __name__ == '__main__':
    arr1 = [1, 2, 3]
    arr2 = [5, 6, 7]
    assert list(MyProduct(arr1, arr2)) == list(product(arr1, arr2))
