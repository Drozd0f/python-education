"""This module contains my zip lazy iterator"""
from additional_practice.lazy_iterators.descriptors import IterableObject


class MyZip:
    """This class describes work my zip lazy iterator"""
    _args = IterableObject('_args')

    def __init__(self, *args: iter):
        self._args = args

    def _shortest_sequence_range(self) -> int:
        return len(sorted(self._args, key=len)[0])

    def _arguments(self):
        for i in range(self._shortest_sequence_range()):
            yield tuple(arg[i] for arg in self._args)

    def __iter__(self):
        return self._arguments()


if __name__ == '__main__':
    names = ['Danilo', 'Vadim', 'Nikita', 'Bogdan']
    ages = [21, 20, 23]
    assert list(MyZip(names, ages)) == list(zip(names, ages))
    assert dict(MyZip(names, ages)) == dict(zip(names, ages))
