#!/usr/bin/python3

"""A module to create a sorted singly linked list

    Raises:
            TypeError

    Todo: Create a singly linked list
"""


class Node:
    """A class to make a node for the singly linked list

    Attributes:
            data (private): store the value of each node
            next_node (private): The next node in the linked list
    """
    def __init__(self, data, next_node=None):
        """Initializing the node attributes

        Args:
            data: the value that the node stores
            next_node: the next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter&setter property

        Raises:
            TypeError: If the value is not of type int

        Returns:
            int: the value that the node stores
        """
        return self.__data

    @property
    def next_node(self):
        """next_node getter&setter property

        Raises:
            TypeError: If the value is not of type Node or None

        Returns:
            Node: the next node in the linked list
        """
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
    """A class to create a singly linked list

    Attributes:
        head (private): the head node of the linked list
    """

    def __init__(self):
        """Initializing the head node to None
        """
        self.__head = None

    def __str__(self):
        """customize the print statement to print the linked list nicly

        Returns:
            string: the data of the linked list each node in a row
        """
        data = ''
        node = self.__head
        while (node is not None):
            data += str(node.data)
            if node.next_node is not None:
                data += '\n'
            node = node.next_node

        return data

    def sorted_insert(self, value):
        """Insert the node in right sorted position in the linked list

        Args:
            value (int): the data of the node to be inserted
        """
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
