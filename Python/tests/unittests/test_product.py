"""This module contains test class Product for exercise Unittesting"""
import typing as t

import pytest

from unittesting.to_test import Product


@pytest.mark.parametrize(
    'title, price, quantity, expected_res',
    [
        ('ketchup', 12, None, ('ketchup', 12, 1)),
        ('ketchup', 12, 23, ('ketchup', 12, 23))
    ]
)
def test_init(title, price, quantity, expected_res):
    """This test contest check constructor class Product"""
    if quantity is None:
        product = Product(title, price)
    else:
        product = Product(title, price, quantity)
    assert product.title == expected_res[0]
    assert product.price == expected_res[1]
    assert product.quantity == expected_res[2]


@pytest.mark.parametrize(
    'num', [None, 5, 10, 15]
)
def test_subtract_quantity(product_object: Product, num: t.Optional[int]):
    """This test contest check method subtract_quantity class Product"""
    if num is None:
        num = 1
        expected_quantity = product_object.quantity - num
        product_object.subtract_quantity()
    else:
        expected_quantity = product_object.quantity - num
        product_object.subtract_quantity(num)
    assert product_object.quantity == expected_quantity


@pytest.mark.parametrize(
    'num', [None, 5, 10, 15]
)
def test_add_quantity(product_object: Product, num: t.Optional[int]):
    """This test contest check method add_quantity class Product"""
    if num is None:
        num = 1
        expected_quantity = product_object.quantity + num
        product_object.add_quantity()
    else:
        expected_quantity = product_object.quantity + num
        product_object.add_quantity(num)
    assert product_object.quantity == expected_quantity


@pytest.mark.parametrize(
    'num', [1, 5, 10, 15]
)
def test_change_price(product_object: Product, num: int):
    """This test contest check method change_price class Product"""
    product_object.change_price(num)
    assert product_object.price == num
