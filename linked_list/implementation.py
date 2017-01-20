from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        # [Node(1)==[headNode] -> Node(2) -> Node(3) -> end]
        self.start = None
        self.end = None
        self.elems = []
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        elements = []

        for elem in self:
            elements.append(elem)

        return str(elements)

    def __len__(self):
        length = 0
        for elem in self:
            length += 1
        return length

    def __iter__(self):
        node = self.start
        while node:
            yield node.elem
            node = node.next
        raise StopIteration

    def __getitem__(self, index):
        if index > len(self) - 1:
            raise IndexError

        prev_node = None
        current_node = self.start

        for i in range(0, index):
            prev_node = current_node
            current_node = current_node.next

        return current_node.elem

    def __add__(self, other):
        new = LinkedList([elem for elem in self])
        for i in other:
            new.append(i)
        return new

    def __iadd__(self, other):
        for i in other:
            self.append(i)
        return self

    def __eq__(self, other):
        if other.start is None and self.start is None:
            return True
        if other.start is None or self.start is None:
            return False

        n1 = self.start
        n2 = other.start
        if len(self) == len(other):
            while True:
                if n1.elem != n2.elem:
                    return False
                if n1.next is None:
                    return True
                n1 = n1.next
                n2 = n2.next

        return False

    def __ne__(self, other):
        return not self == other

    def append(self, elem):
        # first node
        if self.start is None:
            self.start = Node(elem)
            self.end = self.start
            return self.start

        new_node = Node(elem)
        self.end.next = new_node
        self.end = new_node

    def count(self):
        return len(self)

    def pop(self, index=None):
        # pop on empty linkedlist or invalid index

        if index is None:
            index = len(self) - 1

        if len(self) == 0 or index >= len(self):
            raise IndexError

        # removing first item
        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem

        # single item list
        if len(self) == 1:
            elem = self.end.elem
            self.start = None
            self.end = None
            return elem

        # removing last item
        if index == len(self) - 1:
            prev_node = None
            current_node = self.start

            for elem in self:
                if elem == self.end.elem:
                    self.end = prev_node
                    self.end.next = None
                    continue
                prev_node = current_node
                current_node = current_node.next

            return current_node.elem

        # item in middle of list
        if index < len(self) - 1:
            prev_node = None
            current_node = self.start

            for i in range(0, index):
                prev_node = current_node
                current_node = current_node.next

            elem = current_node.elem
            prev_node.next = current_node.next

            return elem
