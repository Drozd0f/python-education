"""This module contains test Queue for exercise Data Structures - practice"""
import pytest

from data_structures.my_queue import Queue


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_enqueue(queue_obj: Queue, value: int):
    """This test check method enqueue Queue data structures"""
    queue_obj.enqueue(value)
    assert queue_obj.tail.val == value


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_dequeue(queue_obj: Queue, value: int):
    """This test check method dequeue Queue data structures"""
    queue_obj.enqueue(value)
    queue_obj.dequeue()
    res = queue_obj.dequeue()
    assert res == value


@pytest.mark.parametrize(
    'value',
    [(val, val + 1) for val in range(40) if val != 21]
)
def test_peek(queue_obj: Queue, value: int):
    """This test check method peek Queue data structures"""
    queue_obj.enqueue(value)
    queue_obj.dequeue()
    assert queue_obj.peek() == value
