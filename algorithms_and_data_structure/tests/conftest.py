"""This module contains configure file for exercise Algorithms And Data Structure"""
import pytest

from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.my_queue import Queue
from data_structures.graph import Graph
from data_structures.binary_search_tree import BinarySearchTree
from data_structures.hash_table import HashTable


@pytest.fixture
def linked_list_obj() -> LinkedList:
    """This fixture returns object of class LinkedList"""
    return LinkedList(21)


@pytest.fixture
def stack_obj() -> Stack:
    """This fixture returns object of class Stack"""
    return Stack(21)


@pytest.fixture
def queue_obj() -> Queue:
    """This fixture returns object of class Queue"""
    return Queue(21)


@pytest.fixture
def graph_obj() -> Graph:
    """This fixture returns object of class LinkedList"""
    return Graph(21)


@pytest.fixture
def binary_search_tree_obj() -> BinarySearchTree:
    """This fixture returns object of class Stack"""
    return BinarySearchTree(21)


@pytest.fixture
def hash_table_obj() -> HashTable:
    """This fixture returns object of class Queue"""
    return HashTable()
