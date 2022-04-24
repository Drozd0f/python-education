"""This module contains test class Shop for exercise Unittesting"""
import typing as t

import pytest

from unittesting.to_test import Shop, Product


@pytest.mark.parametrize(
    'products', [
        None, Product('ketchup', 12, 23)
    ]
)
def test_init(products):
    """This test contest check constructor class Shop"""
    shop = Shop(products)
    if products is None:
        expected_res = []
    else:
        expected_res = [products]
    assert shop.products == expected_res


def test_add_product(shop_object: Shop):
    """This test contest check method add_product class Shop"""
    products_list = [
        Product('ketchup', 12, 23),
        Product('mayonnaise', 21, 10),
        Product('ketchup', 34, 1),
    ]
    for products in products_list:
        shop_object.add_product(products)
        assert products in shop_object.products
    assert shop_object.products == products_list


def test_sell_product_success(shop_sell_product_object: Shop, product_object: Product):
    """This test contest success check method sell_product class Shop"""
    expected_receipt = product_object.quantity * product_object.price
    expected_money = shop_sell_product_object.money + expected_receipt
    receipt = shop_sell_product_object.sell_product(product_object.title, product_object.quantity)
    assert receipt == expected_receipt
    assert shop_sell_product_object.money == expected_money


def test_sell_product_idx_none(shop_object: Shop, product_object: Product):
    """This test contest check method sell_product class Shop if product not in Shop"""
    assert shop_object.sell_product(product_object.title) is None


@pytest.mark.parametrize(
    'products, qty_to_sell', [
        (Product('ketchup', 12, 0), None),
        (Product('mayonnaise', 21, 10), 24),
        (Product('ketchup', 34, 1), 2)
    ]
)
def test_sell_product_quantity_bad(shop_object: Shop, products: Product,
                                   qty_to_sell: t.Optional[int]):
    """This test contest check method sell_product class Shop
    if specified quantity > product quantity
    """
    shop_object.add_product(products)
    with pytest.raises(ValueError) as excinfo:
        if qty_to_sell is None:
            shop_object.sell_product(products.title)
        else:
            shop_object.sell_product(products.title, qty_to_sell)
    assert str(excinfo.value) == 'Not enough products'


@pytest.mark.parametrize(
    'products, qty_to_sell', [
        (Product('ketchup', 12, 1), None),
        (Product('mayonnaise', 21, 24), 24),
        (Product('ketchup', 34, 2), 2)
    ]
)
def test_sell_product_quantity_eq_qty(shop_object: Shop, products: Product,
                                      qty_to_sell: t.Optional[int]):
    """This test contest check method sell_product class Shop
    if specified quantity == product quantity
    """
    shop_object.add_product(products)
    qty = 1 if qty_to_sell is None else qty_to_sell
    expected_receipt = products.price * qty
    expected_money = shop_object.money + expected_receipt
    if qty_to_sell is None:
        receipt = shop_object.sell_product(products.title, 1)
    else:
        receipt = shop_object.sell_product(products.title, qty_to_sell)
    assert products not in shop_object.products
    assert receipt == expected_receipt
    assert shop_object.money == expected_money


@pytest.mark.parametrize(
    'products, qty_to_sell', [
        (Product('ketchup', 12, 2), None),
        (Product('mayonnaise', 21, 26), 25),
        (Product('ketchup', 34, 4), 3)
    ]
)
def test_sell_product_quantity_neq_qty(shop_object: Shop, products: Product,
                                       qty_to_sell: t.Optional[int]):
    """This test contest check method sell_product class Shop
    if specified quantity < product quantity
    """
    shop_object.add_product(products)
    qty_to_sell = 1 if qty_to_sell is None else qty_to_sell
    expected_receipt = products.price * qty_to_sell
    expected_money = shop_object.money + expected_receipt
    expected_quantity = products.quantity - qty_to_sell
    receipt = shop_object.sell_product(products.title, qty_to_sell)
    assert receipt == expected_receipt
    assert shop_object.money == expected_money
    assert products.quantity == expected_quantity
