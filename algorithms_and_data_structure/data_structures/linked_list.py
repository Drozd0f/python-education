"""This module contains LinkedList for exercise Data Structures - practice"""
import typing as t

from data_structures.base_linked_list import BaseLinkedList


class LinkedList(BaseLinkedList):
    """This class describes LinkedList structure"""
    def append(self, val):
        """This method adds a value to the end of the list"""
        self._append(val)

    def prepend(self, val):
        """This method adds a value to the beginning of the list"""
        self._prepend(val)

    def lookup(self, val) -> t.Optional[int]:
        """This method finds the index of an element by value"""
        return self._lookup(val)

    def insert(self, idx: int, val):
        """This method inserts an element at a specific index, shifting the elements to the right"""
        self._insert(idx, val)

    def delete(self, idx):
        """This method removes an element by index"""
        self._delete(idx)


if __name__ == '__main__':
    linked_list = LinkedList(5)
    print(f'Create: {linked_list}')
    linked_list.prepend(1)
    print(f'Preapend: {linked_list}')
    linked_list.append(2)
    print(f'Append: {linked_list}')
    print(f'Lookup: {linked_list.lookup(1)}')
    linked_list.insert(0, 10)
    print(f'Insert: {linked_list}')
    linked_list.delete(0)
    print(f'Delete: {linked_list}')
