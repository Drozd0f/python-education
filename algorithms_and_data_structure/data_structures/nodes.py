"""This module contains Nodes for exercise Data Structures - practice"""


class Node:
    """This class describes Node for BaseLinkedList and its implementations"""
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def __str__(self):
        return f'Node(val={self.val}, next={self.next_node})'


class HashTableNode:
    """This class describes Node for HashTable"""
    def __init__(self, key, val, next_node=None):
        self.key = key
        self.val = val
        self.next_node = next_node

    def __str__(self):
        return f'HashTableNode(key={self.key}, val={self.val}, next={self.next_node})'


class TreeNode:
    """This class describes Node for BinarySearchTree"""
    val = None
    left_node = None
    right_node = None

    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node

    def count_child(self) -> int:
        """This method return count child TreeNode"""
        count = 0
        if self.left_node is not None:
            count += 1
        if self.right_node is not None:
            count += 1
        return count

    def busy_child(self):
        """This method return busy TreeNode if it exists"""
        if self.left_node is not None:
            return self.left_node
        return self.right_node

    def __str__(self):
        return f'TreeNode(val={self.val}, left_node={self.left_node}, right_node={self.right_node})'
