"""This module contains the implementation of the fibonacci number generator"""
#  Example 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
import unittest


def fib(count: int):
    """This function describes implementation of the fibonacci number generator"""
    first_num = 0
    lust_num = 1
    while count != 0:
        yield first_num
        first_num, lust_num = lust_num, first_num + lust_num
        count -= 1


class TestFibNumber(unittest.TestCase):
    """This class describes testing fibonacci number generator"""
    expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    def test_fib(self):
        """This test describes checking the operation of the generator"""
        for idx, fib_num in enumerate(fib(len(self))):
            assert self[idx] == fib_num

    def __len__(self) -> int:
        return len(self.expected_result)

    def __getitem__(self, idx) -> int:
        return self.expected_result[idx]


if __name__ == '__main__':
    unittest.main()
