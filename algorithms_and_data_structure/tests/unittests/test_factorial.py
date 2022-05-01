"""This module contains test recursive factorial implementation
for exercise Algorithms - practice
"""
import math
import random

import pytest

from algorithms.factorial import factorial as my_factorial


@pytest.mark.parametrize(
    'number',
    [
        random.randint(0, 100) for _ in range(40)
    ]
)
def test_success(number: int):
    """This test check success work function my_factorial"""
    assert my_factorial(number) == math.factorial(number)


@pytest.mark.parametrize(
    'number',
    [
        random.randint(-100, -1) for _ in range(40)
    ]
)
def test_negative_number(number):
    """This test check value_error got negative number in function my_factorial"""
    with pytest.raises(ValueError) as excinfo:
        my_factorial(number)
    assert excinfo.type is ValueError
    assert str(excinfo.value) == 'factorial() not defined for negative values'
