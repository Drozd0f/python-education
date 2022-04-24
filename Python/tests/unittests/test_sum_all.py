"""This module contains test function sum_all for exercise Unittesting"""
from unittesting.to_test import sum_all


def test_sum_all(random_list: list):
    """This test contest check function sum_all"""
    assert sum_all(*random_list) == sum(random_list)
