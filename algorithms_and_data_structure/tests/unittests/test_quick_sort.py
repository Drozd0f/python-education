"""This module contains test quick sort for exercise Algorithms - practice"""
import random

import pytest

from algorithms.quick_sort import quick_sort


@pytest.mark.parametrize(
    'array',
    [
        [random.randint(-100, 100) for _ in range(20)]
        for _ in range(20)
    ]
)
def test_success(array):
    """This test check success work function quick_sort"""
    assert quick_sort(array) == sorted(array)
