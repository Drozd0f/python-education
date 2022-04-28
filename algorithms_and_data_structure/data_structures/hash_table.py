"""This module contains HashTable for exercise Data Structures - practice"""
import re
import ctypes
import typing as t

from data_structures.linked_list import LinkedList
from data_structures.nodes import HashTableNode


class HashTable:
    """This class describes HashTable structure"""
    _values: LinkedList = LinkedList(None)
    _items = ''
    _pattern_value = '{hash_key}=\\d+'

    def __init__(self):
        for key in range(30):
            if key != 29:
                self._items += f'{key}={id(None)}, '
            else:
                self._items += f'{key}={id(None)}'

    def _hash(self, key: str) -> int:
        res = 0
        for char in str(key):
            if char.isdigit():
                res += int(char)
            else:
                res += ord(char)
        return res % 30

    def _find_hash_table_node(self, hash_key: int) -> str:
        hash_table_node = re.findall(self._pattern_value.format(hash_key=hash_key), self._items)
        return hash_table_node[0]

    def _get_hash_table_node(self, hash_key: int) -> t.Optional[HashTableNode]:
        hash_table_node_id = self._find_hash_table_node(hash_key)
        _id = int(re.sub(r'\d+=', '', hash_table_node_id))
        return ctypes.cast(_id, ctypes.py_object).value

    def _save_value(self, hash_key: int, key, val):
        hash_table_node = self._get_hash_table_node(hash_key)
        if hash_table_node is None:
            node = HashTableNode(key, val)
            self._values.append(node)
            id_new_item = id(node)
            new_value = re.sub(r'\d+$', f'{id_new_item}', self._find_hash_table_node(hash_key))
            self._items = re.sub(
                self._pattern_value.format(hash_key=hash_key),
                new_value,
                self._items
            )
        else:
            hash_table_node.next_node = HashTableNode(key, val)

    def _find_key(self, hash_table_node: HashTableNode, key) -> t.Optional[HashTableNode]:
        while hash_table_node is not None:
            if hash_table_node.key == key:
                return hash_table_node
            hash_table_node = hash_table_node.next_node

    def _delete_eny_node(self, node: HashTableNode, key):
        parent_node = node
        node = node.next_node
        while node is not None:
            if node.key == key:
                parent_node.next_node = node.next_node
            node = node.next_node

    def _delete_key(self, node: HashTableNode, key):
        found_node = self._find_key(node, key)
        if found_node is None:
            raise KeyError
        if found_node.key == key:
            new_node = found_node.next_node
            hash_key = self._hash(key)
            new_value = re.sub(r'\d+$', f'{id(new_node)}', self._find_hash_table_node(hash_key))
            self._items = re.sub(
                self._pattern_value.format(hash_key=hash_key),
                new_value,
                self._items
            )
            idx = self._values.lookup(found_node)
            self._values.delete(idx)
            self._values.append(new_node)
        else:
            self._delete_eny_node(node, key)

    def insert(self, key, val):
        """This method adds value with key"""
        self._save_value(self._hash(key), key, val)

    def lookup(self, key):
        """This method returns value by key"""
        hash_table_node = self._get_hash_table_node(self._hash(key))
        if hash_table_node is None:
            raise KeyError
        found_node = self._find_key(hash_table_node, key)
        if found_node is None:
            raise KeyError
        return found_node.val

    def delete(self, key):
        """This method delete value by key"""
        hash_table_node = self._get_hash_table_node(self._hash(key))
        if hash_table_node is None:
            raise KeyError
        self._delete_key(hash_table_node, key)


if __name__ == '__main__':
    table = HashTable()
    table.insert('Danilo', 21)
    table.insert('Danilo', 10)
    table.insert('Vova', 30)
    table.insert(22, 22)
    print(table.lookup('Danilo'))
    print(table.lookup('Vova'))
    print(table.lookup(22))
    table.delete(22)
