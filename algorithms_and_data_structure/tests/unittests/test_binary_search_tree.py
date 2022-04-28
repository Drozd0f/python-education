"""This module contains test HashTable for exercise Data Structures - practice"""
import pytest

from data_structures.binary_search_tree import BinarySearchTree


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_insert(binary_search_tree_obj: BinarySearchTree, value: int):
    """This test check method insert BinarySearchTree data structures"""
    binary_search_tree_obj.insert(value)
    if value < binary_search_tree_obj.root.val:
        assert binary_search_tree_obj.root.left_node.val == value
    else:
        assert binary_search_tree_obj.root.right_node.val == value


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_lookup(binary_search_tree_obj: BinarySearchTree, value: int):
    """This test check method lookup BinarySearchTree data structures"""
    binary_search_tree_obj.insert(value)
    assert binary_search_tree_obj.lookup(value).val == value


@pytest.mark.parametrize(
    'value',
    list(range(-20, 20))
)
def test_delete(binary_search_tree_obj: BinarySearchTree, value: int):
    """This test check method delete BinarySearchTree data structures"""
    binary_search_tree_obj.insert(value)
    binary_search_tree_obj.delete(value)
    if value < binary_search_tree_obj.root.val:
        assert binary_search_tree_obj.root.left_node is None
    else:
        assert binary_search_tree_obj.root.right_node is None
