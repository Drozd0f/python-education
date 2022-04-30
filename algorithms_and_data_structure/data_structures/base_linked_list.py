"""This module contains BaseLinkedList for exercise Data Structures - practice"""
from abc import ABC
import typing as t

from data_structures.nodes import Node


class BaseLinkedList(ABC):
    """This class describes basic linked list"""
    _head: t.Optional[Node] = None
    _tail: t.Optional[Node] = None
    _nodes = 0

    def __init__(self, val):
        node = Node(val)
        self._head = node
        self._tail = node
        self._nodes += 1

    def _prepend(self, val):
        node = Node(val, self._head)
        self._head = node
        self._nodes += 1

    def _append(self, val):
        node = Node(val)
        self._tail.next_node = node
        self._tail = node
        self._nodes += 1

    def _lookup(self, val) -> t.Optional[int]:
        node = self._head
        idx = 0
        while idx != self._nodes:
            if node is None:
                break
            if node.val == val:
                return idx
            idx += 1
            node = node.next_node

    def _insert(self, idx: int, val):
        if abs(idx) > self._nodes:
            raise IndexError
        if idx == 0:
            self._prepend(val)
        else:
            node = self._head
            current_idx = 0
            while current_idx != self._nodes:
                if current_idx == idx - 1:
                    new_node = Node(val, node.next_node)
                    node.next_node = new_node
                    break
                current_idx += 1
                node = node.next_node
        self._nodes += 1

    def _del_head(self):
        self._head = self._head.next_node
        if self._head is None:
            self._tail = self._head

    def _check_tail(self, node: Node, next_node: Node):
        if next_node is self._tail:
            self._tail = node

    def _del_eny_node(self, idx: int):
        node = self._head
        current_idx = 0
        while current_idx != self._nodes:
            if current_idx == idx - 1:
                deleted_node = node.next_node
                self._check_tail(node, deleted_node)
                node.next_node = deleted_node.next_node
                break
            current_idx += 1
            node = node.next_node

    def _delete(self, idx: int):
        if idx < 0 or idx > self._nodes:
            raise IndexError
        if idx == 0:
            self._del_head()
        else:
            self._del_eny_node(idx)
        self._nodes -= 1

    def _iter(self):
        node = self._head
        while node is not None:
            yield node
            node = node.next_node

    @property
    def head(self):
        """This property return head a list"""
        return self._head

    @property
    def tail(self):
        """This property return tail a list"""
        return self._tail

    def __iter__(self):
        return self._iter()

    def __str__(self):
        return f'BaseLinkedList({self._head})'
