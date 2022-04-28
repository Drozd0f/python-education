"""This module contains test LinkedList for exercise Data Structures - practice"""
import random

import pytest

from data_structures.linked_list import LinkedList


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_append(linked_list_obj: LinkedList, value: int):
    """This test check method append LinkedList data structures"""
    linked_list_obj.append(value)
    assert linked_list_obj.tail.val == value
    assert linked_list_obj.tail.next_node is None


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_prepend(linked_list_obj: LinkedList, value: int):
    """This test check method prepend LinkedList data structures"""
    linked_list_obj.prepend(value)
    assert linked_list_obj.head.val == value


@pytest.mark.parametrize(
    'value, count',
    [(val, val + 1) for val in range(40) if val != 21]
)
def test_lookup(linked_list_obj: LinkedList, value: int, count: int):
    """This test check method lookup LinkedList data structures"""
    for test in range(1, count):
        linked_list_obj.append(value - test)
    linked_list_obj.append(value)
    assert linked_list_obj.lookup(value) == count


@pytest.mark.parametrize(
    'value',
    [(val, val) for val in range(-20, 20)]
)
def test_insert(linked_list_obj: LinkedList, value: int):
    """This test check method insert LinkedList data structures"""
    linked_list_obj.append(21)
    random_idx = random.choice(range(0, 3))
    linked_list_obj.insert(random_idx, value)
    assert linked_list_obj.lookup(value) == random_idx


@pytest.mark.parametrize(
    'value',
    [(val, None) for val in range(-20, 20)]
)
def test_delete(linked_list_obj: LinkedList, value: int):
    """This test check method delete LinkedList data structures"""
    linked_list_obj.append(21)
    random_idx = random.choice(range(0, 3))
    linked_list_obj.insert(random_idx, value)
    linked_list_obj.delete(random_idx)
    assert linked_list_obj.lookup(value) is None
