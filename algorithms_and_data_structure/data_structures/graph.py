"""This module contains Graph for exercise Data Structures - practice"""
from data_structures.linked_list import LinkedList


class Graph:
    """This class describes a graph that is undirected and edges without weights"""
    def __init__(self, val):
        self._edges = LinkedList(LinkedList(val))

    def _lookup(self, val) -> LinkedList:
        for vertex in self._edges:
            node = vertex.val
            if node.head.val == val:
                return node
        raise ValueError

    def insert(self, val, *nodes: LinkedList):
        """This method adds a node and links to other nodes by links"""
        vertex = LinkedList(val)
        for node in nodes:
            vertex.append(id(node))
            node.append(id(vertex))
        self._edges.append(vertex)

    def lookup(self, val) -> LinkedList:
        """This method returns a node by value and return a reference to it"""
        return self._lookup(val)

    def delete(self, node: LinkedList):
        """This method removes a node by reference and links to other nodes"""
        for vertex in self._edges:
            idx = vertex.val.lookup(id(node))
            if idx is not None:
                vertex.val.delete(idx)
        deleted_node_idx = self._edges.lookup(node)
        self._edges.delete(deleted_node_idx)

    def __str__(self):
        return f'{self._edges}'


if __name__ == '__main__':
    graph = Graph(5)
    graph.insert(10, graph.lookup(5))
    graph.insert(11, graph.lookup(5), graph.lookup(10))
    graph.delete(graph.lookup(5))
    print(graph.lookup(11))
