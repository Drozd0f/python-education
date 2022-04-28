"""This module contains test Graph for exercise Data Structures - practice"""
import pytest

from data_structures.graph import Graph


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_insert_and_lookup(graph_obj: Graph, value: int):
    """This test check method insert and lookup Graph data structures"""
    old_node = graph_obj.lookup(21)
    graph_obj.insert(value, old_node)
    vertex = graph_obj.lookup(value)
    itr = 0
    for node in vertex:
        if itr == 0:
            assert node.val == value
        else:
            assert node.val == id(old_node)
        itr += 1


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_delete(graph_obj: Graph, value: int):
    """This test check method delete Graph data structures"""
    node = graph_obj.lookup(21)
    graph_obj.insert(value, node)
    graph_obj.delete(graph_obj.lookup(value))
    with pytest.raises(ValueError) as excinfo:
        graph_obj.lookup(value)
    assert excinfo.type is ValueError
