import functools
import random

from list_interface import *


class SimpleNode(NodeInterface):
    def __init__(self, content: object = None, next_node=None):
        super().__init__(content)
        self.next_node = next_node

    def __str__(self):
        return super().__str__() + f", next_node: {self.next_node is not None}"


class SimpleLinkedListIterable(ListIterableInterface):
    def __init__(self, simple_linked_list):
        super().__init__(simple_linked_list)

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        return super().__next__()


class SimpleLinkedList(ListInterface):

    def __init__(self, _list=None):
        self.first_node: SimpleNode = None
        super().__init__(_list)

    def __iter__(self):
        return SimpleLinkedListIterable(self)

    def is_empty(self):
        return self.first_node is None

    def __contains__(self, content):
        if not self.is_empty():
            temp_node = self.first_node
            while temp_node is not None:
                if temp_node.content.__eq__(content):
                    return True
                temp_node = temp_node.next_node
        return False

    def __str__(self):
        output = super().__str__() + "(" + str(self.size()) + "):["
        if self.is_empty():
            output += "]"
            return output
        temp_node = self.first_node
        while temp_node.next_node is not None:
            output += str(temp_node.content) + ", "
            temp_node = temp_node.next_node
        output += str(temp_node.content) + "]"
        return output

    def size(self):
        counter = 0
        temp_node = self.first_node
        while temp_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        return counter

    def add(self, content: object):
        new_node = SimpleNode(content=content)
        if self.is_empty():
            self.first_node = new_node
            return
        temp_node: SimpleNode = self.first_node
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node
        temp_node.next_node = new_node

    @ListInterface.check_index
    def insert(self, index: int, content: object):
        new_node = SimpleNode(content)
        if self.is_empty():
            self.first_node = new_node
            return
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return
        counter = 0
        temp_node = self.first_node
        while counter < index - 1 and temp_node.next_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        new_node.next_node = temp_node.next_node
        temp_node.next_node = new_node

    @ListInterface.check_index
    def set(self, index: int, content: object):
        new_node = SimpleNode(content)
        if self.is_empty():
            self.first_node = new_node
            return
        if index == 0:
            new_node.next_node = self.first_node.next_node
            self.first_node = new_node
            return
        counter = 1
        temp_node = self.first_node
        while counter < index and temp_node.next_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        if temp_node.next_node.next_node is not None:
            new_node.next_node = temp_node.next_node.next_node
        temp_node.next_node = new_node

    @ListInterface.check_empty
    def replace(self, lambda_expression, index=None):
        if index is not None:
            if not 0 <= index < self.size():
                raise IndexError()
        temp_node = self.first_node
        condition = True
        i = 0
        while condition:
            if index is None or index is i:
                temp_node.content = lambda_expression(temp_node.content)
            condition = temp_node.next_node is not None
            temp_node = temp_node.next_node
            i += 1

    def clear(self):
        self.first_node = None

    @ListInterface.check_empty
    def remove(self, content: object):
        temp_node = self.first_node
        if temp_node.content is content:
            self.first_node = temp_node.next_node
            return True
        while temp_node.next_node is not None:
            if temp_node.next_node.content is content:
                temp_node.next_node = temp_node.next_node.next_node
                return True
            temp_node = temp_node.next_node
        return False

    @ListInterface.check_index
    @ListInterface.check_empty
    def pop(self, index):
        output = self.first_node.content
        if index == 0:
            self.first_node = self.first_node.next_node
            return output
        counter = 0
        temp_node = self.first_node
        while temp_node.next_node is not None and counter < index - 1:
            counter += 1
            temp_node = temp_node.next_node
        output = temp_node.next_node.content
        temp_node.next_node = temp_node.next_node.next_node
        return output

    def move(self, element_index, target_index):
        super().move(element_index, target_index)

    def sort(self, asc=True):
        i = 0
        while i < self.size():
            element = self.pop(i)
            j = 0
            while ((self.get(j) <= element) if asc else (self.get(j) > element)) and j < i:
                j += 1
            self.insert(j, element)
            i += 1

    def __reversed__(self):
        if self.size() <= 1:
            return
        counter = 0
        while counter < self.size() - 1:
            self.move(self.size() - 1, counter)
            counter += 1

    def get(self, index: int):
        return self.get_node(index).content

    @ListInterface.check_empty
    def get_node(self, index: int):
        counter = 0
        temp_node = self.first_node
        while counter < index:
            temp_node = temp_node.next_node
            counter += 1
        return temp_node

    def convert(self, _list):
        super().convert(_list)

    def sublist(self, start_index, end_index):
        if start_index < 0 or end_index < start_index or self.size() < end_index:
            raise IndexError()
        counter = 0
        temp_sll = SimpleLinkedList()
        temp_node = self.first_node
        while temp_node.next_node is not None and counter < end_index:
            if start_index <= counter:
                temp_sll.add(temp_node.content)
            temp_node = temp_node.next_node
            counter += 1
        if counter < end_index:
            temp_sll.add(temp_node.content)
        return temp_sll

    def retain_all(self, collection):
        if self.is_empty():
            return None
        temp_sll = SimpleLinkedList()
        temp_node = self.first_node
        while temp_node.next_node:
            if temp_node.content in collection:
                temp_sll.add(temp_node.content)
            temp_node = temp_node.next_node
        if temp_node.content in collection:
            temp_sll.add(temp_node.content)
        return temp_sll


if __name__ == "__main__":
    test_iterable(SimpleLinkedList([1, 2]))

