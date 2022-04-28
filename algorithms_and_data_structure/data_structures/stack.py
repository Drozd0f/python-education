"""This module contains Stack for exercise Data Structures - practice"""
from data_structures.base_linked_list import BaseLinkedList


class Stack(BaseLinkedList):
    """This class describes Stack structure"""
    def push(self, val):
        """This method adds an element to the stack"""
        self._prepend(val)

    def pop(self):
        """This method removes the last element"""
        val = self.tail.val
        self._delete(self._lookup(val))
        return val

    def peek(self):
        """This method returns the value of the top element of the stack"""
        return self.tail.val


if __name__ == '__main__':
    stack = Stack(5)
    print(stack)
    print(stack.peek())
    stack.push(1)
    print(stack)
    stack.pop()
    print(stack)
