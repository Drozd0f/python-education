"""This module contains BinarySearchTree for exercise Data Structures - practice"""
import typing as t

from data_structures.nodes import TreeNode


class BinarySearchTree:
    """This class describes BinarySearchTree structure"""
    _root: t.Optional[TreeNode] = None
    _status = False

    def __init__(self, val):
        self._root = TreeNode(val)

    def _swap_node(self, node: TreeNode, val) -> TreeNode:
        if val < node.val:
            return node.left_node
        return node.right_node

    def _check_node(self, node: TreeNode):
        if node.left_node is node.right_node:
            self._status = False

    def _refactor_solo_node(self, deleted_node: TreeNode) -> t.Optional[TreeNode]:
        if deleted_node.count_child() == 0:
            return None
        return deleted_node.busy_child()

    def _refactor_node(self, deleted_node: TreeNode) -> t.Optional[TreeNode]:
        if deleted_node.count_child() != 2:
            return self._refactor_solo_node(deleted_node)
        _iter = 0
        pre_node = deleted_node
        node = deleted_node.left_node
        while node is not None:
            if node.right_node is None and _iter == 0:
                deleted_node.val = node.val
                pre_node.left_node = node.busy_child()
                return deleted_node
            if node.right_node is None and _iter != 0:
                deleted_node.val = node.val
                pre_node.right_node = node.busy_child()
                return deleted_node
            pre_node = node
            node = node.right_node
            _iter += 1

    def _delete_root(self):
        self._root = self._refactor_node(self._root)

    def _delete_eny_node(self, val):
        node = self._root
        self._status = True
        while self._status:
            if node.left_node is not None and val == node.left_node.val:
                node.left_node = self._refactor_node(node.left_node)
                break
            if node.right_node is not None and val == node.right_node.val:
                node.right_node = self._refactor_node(node.right_node)
                break
            self._check_node(node)
            node = self._swap_node(node, val)

    def insert(self, val):
        """This method adds an element"""
        node = self._root
        while True:
            if val < node.val and node.left_node is None:
                node.left_node = TreeNode(val)
                break
            if val >= node.val and node.right_node is None:
                node.right_node = TreeNode(val)
                break
            node = self._swap_node(node, val)

    def lookup(self, val) -> TreeNode:
        """This method finds an element by value and returns a reference to it"""
        node = self._root
        self._status = True
        while self._status:
            if node.val == val:
                return node
            self._check_node(node)
            node = self._swap_node(node, val)

    def delete(self, val):
        """This method removes an element by value"""
        if self._root.val == val:
            self._delete_root()
        else:
            self._delete_eny_node(val)

    @property
    def root(self):
        """This property return root of tree"""
        return self._root

    def __str__(self):
        return f'{self._root}'


if __name__ == '__main__':
    binary_search_tree = BinarySearchTree(1)
    print(binary_search_tree)
    binary_search_tree.insert(10)
    binary_search_tree.insert(15)
    binary_search_tree.insert(5)
    binary_search_tree.insert(2)
    binary_search_tree.insert(6)
    binary_search_tree.insert(7)
    print(binary_search_tree)
    binary_search_tree.delete(1)
    print(binary_search_tree)
    binary_search_tree.delete(10)
    print(binary_search_tree)
