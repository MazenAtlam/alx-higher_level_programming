#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')

        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        data = ''
        node = self.__head
        while (node is not None):
            data += str(node.data)
            if node.next_node is not None:
                data += '\n'
            node = node.next_node

        return data

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or new_node.data <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while (node.next_node is not None
                   and new_node.data > node.next_node.data):
                node = node.next_node

            new_node.next_node = node.next_node
            node.next_node = new_node
