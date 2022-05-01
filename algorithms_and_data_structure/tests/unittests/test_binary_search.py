"""This module contains test binary search for exercise Algorithms - practice"""
import random

import pytest

from algorithms.binary_search import binary_search


@pytest.mark.parametrize(
    'array',
    [
        sorted(random.sample(range(-100, 100), 20))
        for _ in range(20)
    ]
)
def test_success(array: list):
    """This test check success work function binary_search"""
    number_search = random.choice(array)
    expected_idx = array.index(number_search)
    assert binary_search(array, number_search) == expected_idx


@pytest.mark.parametrize(
    'array',
    [
        [random.randint(-100, 100) for _ in range(20)]
        for _ in range(20)
    ]
)
def test_value_error(array):
    """This test check value_error unsorted list in function binary_search"""
    number_search = random.choice(array)
    with pytest.raises(ValueError) as excinfo:
        binary_search(array, number_search)
    assert excinfo.type is ValueError
    assert str(excinfo.value) == f'{array} don\'t sorted list'
