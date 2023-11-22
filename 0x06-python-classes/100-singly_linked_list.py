#!/usr/bin/python3
"""This module implements a Singly linked list using class"""


class Node:
    """class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """Initilize node

        Args:
            data (int): integer data to be stored in the node
            next_node (Node, optional): the next node in the list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for __data

        Returns:
            int: integer data stored in __data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for __data

        Args:
            value (int): integer data stored in the node

        Raises:
            TypeError: data must be an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for __next_node

        Returns:
            Node: the next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for __next_node

        Args:
            value (Node): sets the next node

        Raises:
            TypeError: next_node must be a Node object
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return str(self.__data)


class SinglyLinkedList:
    """Represents a single linked list

    Attributes:
        __head (Node): head of the linked list
    """
    def __init__(self):
        """Initializes the linked list

        Returns:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts value in a sorted position

        Args:
            value (int): data stored inside the new node

        Returns:
            None
        """
        new_node = Node(value)
        temp = self.__head
        if temp is None or temp.data >= value:
            if temp:
                new_node.next_node = temp
            self.__head = new_node
            return
        while temp.next_node is not None:
            if temp.next_node.data >= value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __str__(self):
        """String representation of SinglyLinkedList instance

        Returns:
            Formatted string representing the linked list
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp)
            if temp.next_node is not None:
                string += "\n"
            temp = temp.next_node
        return string
