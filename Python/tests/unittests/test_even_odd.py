"""This module contains test function even_odd for exercise Unittesting"""
import pytest

from unittesting.to_test import even_odd


@pytest.mark.parametrize(
    'number, expected_res',
    [
        (1, 'odd'),
        (2, 'even'),
        (3, 'odd'),
        (4, 'even'),
        (5, 'odd'),
        (6, 'even'),
        (7, 'odd'),
        (8, 'even'),
        (9, 'odd'),
        (10, 'even'),
    ]
)
def test_even_odd(number, expected_res):
    """This test contest check function even_odd"""
    assert even_odd(number) == expected_res
