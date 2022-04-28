"""This module contains test Stack for exercise Data Structures - practice"""
import pytest

from data_structures.stack import Stack


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_push(stack_obj: Stack, value: int):
    """This test check method push Stack data structures"""
    stack_obj.push(value)
    assert stack_obj.head.val == value


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_pop(stack_obj: Stack, value: int):
    """This test check method prepend Stack data structures"""
    stack_obj.push(value)
    stack_obj.pop()
    res = stack_obj.pop()
    assert res == value


@pytest.mark.parametrize(
    'value',
    [val for val in range(40) if val != 21]
)
def test_peek(stack_obj: Stack, value: int):
    """This test check method peek Stack data structures"""
    stack_obj.push(value)
    stack_obj.pop()
    assert stack_obj.peek() == value
