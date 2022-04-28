"""This module contains Queue for exercise Data Structures - practice"""
from data_structures.base_linked_list import BaseLinkedList


class Queue(BaseLinkedList):
    """This class describes Queue structure"""
    def enqueue(self, val):
        """This method adds an element to the end of the queue"""
        self._append(val)

    def dequeue(self):
        """This method removes an element from the front of the queue"""
        val = self.head.val
        self._delete(0)
        return val

    def peek(self):
        """This method returns the value of the element at the head of the queue"""
        return self.head.val


if __name__ == '__main__':
    # queue = Queue(5)
    # print(queue)
    # print(queue.peek())
    # queue.enqueue(1)
    # print(queue)
    # queue.dequeue()
    # print(queue)
    pass
