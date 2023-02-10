import random
from ctypes import Array

index_error_message = "Index is not allowed to be lower 0 or higher the size (included)"


#   Nodes for Simple- and DoubleLinkedList

class SimpleNode:
    def __init__(self, content: object = None, next_node=None):
        self.content = content
        self.next_node = next_node


class SimpleLinkedListIterable:
    def __init__(self, simple_linked_list):
        self.__linked_list = simple_linked_list
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < self.__linked_list.size():
            result = self.__linked_list.get(self.__index)
            self.__index += 1
            return result
        raise StopIteration


#   LinkedList-classes

#   TODO:   Inspiration for which methods are needed:
#           https://www.digitalocean.com/community/tutorials/java-list
#   TODO: Idea, instead of temp_node.next_node use recursion
class SimpleLinkedList:

    #   TODO:   Constructor

    def __init__(self):
        self.first_node: SimpleNode = None

    #   TODO:   Methods to move through the list (iterable)

    def __iter__(self):
        #   For looping through "for content in linkedlist" or checking for content "content in linkedlist"
        return SimpleLinkedListIterable(self)

    #   TODO:   Methods to check the list.

    def is_empty(self):
        #   Checking if the list is empty
        return self.first_node is None

    def contains(self, content):
        #   Checking if at least one element is the same as the given content
        if not self.is_empty():
            temp_node = self.first_node
            while temp_node is not None:
                if temp_node.content.__eq__(content):
                    return True
                temp_node = temp_node.next_node
        return False

    #   TODO:   Methods giving information about the list.

    def __str__(self):
        #   to-string
        output = self.__class__.__name__ + "(" + str(self.size()) + "):["
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
        #   Returns the length of the list (excluding multidimensional list)
        counter = 0
        temp_node = self.first_node
        while temp_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        return counter

    #   TODO:   Methods changing the list.

    def add(self, content: object):
        #   Adds new content to the end of the last
        new_node = SimpleNode(content=content)
        if self.is_empty():
            self.first_node = new_node
            return
        temp_node: SimpleNode = self.first_node
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node
        temp_node.next_node = new_node

    def insert(self, index: int, content: object):
        #   Inserts new content on the given index
        if index < 0 or self.size() < index:
            raise IndexError(index_error_message)
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

    def set(self, index: int, content: object):
        #   Replaces old content with new content on given index
        if index < 0 or self.size() <= index:
            raise IndexError(index_error_message)
        new_node = SimpleNode(content)
        if self.is_empty():
            self.first_node = new_node
            return
        if index == 0:
            new_node.next_node = self.first_node.next_node
            self.first_node = new_node
            return
        counter = 0
        temp_node = self.first_node
        while counter < index - 1 and temp_node.next_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        if temp_node.next_node.next_node is not None:
            new_node.next_node = temp_node.next_node.next_node
        temp_node.next_node = new_node

    def replace(self, index, lambda_expression):
        #   Replaces content by using lambda-expression on it.
        self.set(index, lambda_expression(self.get(index)))

    def replace_all(self, lambda_expression):
        #   Inspiration: https://www.w3schools.com/python/python_lambda.asp
        #   Replaces element in the list by using lambda-expression on each element.
        if self.is_empty():
            return
        temp_node = self.first_node
        condition = True
        while condition:
            temp_node.content = lambda_expression(temp_node.content)
            condition = temp_node.next_node is not None
            temp_node = temp_node.next_node

    def clear(self):
        #   Clears the list
        self.first_node = None

    def remove(self, content: object):
        if self.is_empty():
            return False
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

    def pop(self, index):
        if self.is_empty():
            return
        if index < 0 or self.size() <= index:
            raise IndexError
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
        self.insert(target_index, self.pop(element_index))

    # TODO: Insertion-sort

    def insertion_sort(self, asc=True):
        i = 0
        while i < self.size():
            element = self.pop(i)
            j = 0
            while ((self.get(j) <= element) if asc else (self.get(j) > element)) and j < i:
                j += 1
            self.insert(j, element)
            i += 1

    def __reversed__(self):
        #   Turns order of the list
        if self.size() <= 1:
            return
        counter = 0
        while counter < self.size() - 1:
            self.move(self.size() - 1, counter)
            counter += 1

    #   TODO:   Methods returning list-content (or nodes, hidden from outside-code)

    def get(self, index: int):
        #   Returns content at the given index.
        return self.__get_node(index).content

    def __get_node(self, index: int):
        #   Returns node at given index.
        #   Not visible outside SimpleLinkedList-class.
        if self.size() == 0 or index < 0 or self.size() <= index:
            raise IndexError(index_error_message)
        counter = 0
        temp_node = self.first_node
        while counter < index:
            temp_node = temp_node.next_node
            counter += 1
        return temp_node

    def to_list(self):
        #   Returns content in a normal list.
        if self.is_empty():
            return ()
        temp_node = self.first_node
        temp = []
        while temp_node is not None:
            temp.append(temp_node.content)
            temp_node = temp_node.next_node
        return temp

    def sublist(self, start_index, end_index):
        #   Returns content between start_index (included) and end_index (excluded) as a SimpleLinkedList.
        if start_index < 0 or end_index < start_index or self.size() < end_index:
            raise IndexError(index_error_message)
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
        #   Returns a LinkedList matching the content in the current linkedlist and the given collection.
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


class DualNode(SimpleNode):
    def __init__(self, content: object = None, next_node=None, previous_node=None):
        super().__init__(content=content, next_node=next_node)
        self.previous_node = previous_node


class DualLinkedListIterable(SimpleLinkedListIterable):
    def __init__(self, dual_linked_list):
        super().__init__(simple_linked_list=dual_linked_list)

    def __iter__(self):
        return self

    def __previous__(self):
        if 0 < super().__index:
            result = super().__linked_list.get(self.__index)
            super().__index -= 1
            return result
        raise StopIteration


# TODO: To finish later.
class DoubleLinkedList(SimpleLinkedList):
    def __init__(self):
        super().__init__()
        self.last_node: DualNode = None

    def __iter__(self):
        return DualLinkedListIterable(self)

    def is_empty(self):
        return super().is_empty() and self.last_node is None

    def contains(self, content):
        return super().contains()

    def __str__(self):
        return super().__str__()

    def size(self):
        return super().size()

    def add(self, content: object):
        new_node = DualNode(content=content)
        if self.is_empty():
            self.first_node = new_node
            self.last_node = new_node
            return
        self.last_node.next_node = new_node
        new_node.previous_node = self.last_node
        self.last_node = new_node

    def insert(self, index: int, content: object):
        if index < self.size():
            pass

    def set(self, index: int, content: object):
        pass

    def replace(self, index, lambda_expression):
        pass

    def replace_all(self, lambda_expression):
        pass

    def clear(self):
        super().clear()
        self.last_node = None

    def remove(self, content: object):
        pass

    def pop(self, index):
        pass

    def move(self, element_index, target_index):
        self.insert(target_index, self.pop(element_index))

    def insertion_sort(self, asc=True):
        pass

    def __reversed__(self):
        pass

    def get(self, index: int):
        pass

    def __get_node(self, index: int):
        pass

    def to_list(self):
        pass

    def sublist(self, start_index, end_index):
        pass

    def retain_all(self, collection):
        pass


class ArrayList:
    def __init__(self, size: int = 25):
        self.values: Array = ()
        print(type(self.values))


def simple_linkedlist_example(amount: int = 1000):
    sl_list = SimpleLinkedList()
    for i in range(amount):
        sl_list.add(random.randint(-amount, amount))
    for i in range(sl_list.size()):
        print(sl_list.get(i))
    return sl_list


dll = DoubleLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
print(dll)
