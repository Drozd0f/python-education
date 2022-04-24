"""This module contains test function time_of_day for exercise Unittesting"""
import pytest
from freezegun.api import FrozenDateTimeFactory

from unittesting.to_test import time_of_day


@pytest.mark.parametrize(
    'time, expected_res',
    [
        ('2022-04-23-00', 'night'),
        ('2022-04-23-05', 'night'),
        ('2022-04-23-18', 'night'),
        ('2022-04-23-06', 'morning'),
        ('2022-04-23-11', 'morning'),
        ('2022-04-23-12', 'afternoon'),
        ('2022-04-23-17', 'afternoon'),
    ]
)
def test_time_of_day(freezer: FrozenDateTimeFactory, time, expected_res):
    """This test contest check function time_of_day"""
    freezer.move_to(time)
    assert time_of_day() == expected_res
