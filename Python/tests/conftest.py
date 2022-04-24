"""This module contains configure file for exercise Unittesting"""
import random

import pytest

from unittesting.to_test import Shop, Product


@pytest.fixture
def random_list() -> list:
    """This fixture returns a random list of 20 numbers"""
    return [random.randrange(-10, 10) for _ in range(20)]


@pytest.fixture
def product_object() -> Product:
    """This fixture returns object of class Product"""
    return Product('ketchup', 12, 23)


@pytest.fixture
def shop_object() -> Shop:
    """This fixture returns object of class Shop"""
    return Shop()


@pytest.fixture
def shop_sell_product_object(product_object) -> Shop:  # pylint: disable=W0621 (redefined-outer-name)
    """This fixture returns object of class Shop which contains
    products = List[Product]
    """
    return Shop(product_object)
