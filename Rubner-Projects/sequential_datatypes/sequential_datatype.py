import random
from ctypes import Array


class NodeInterface:
    def __init__(self, content: object = None):
        self.content = content


class ListIterableInterface:
    class ListIterableInterface:
        def __init__(self, list_interface):
            self.__list_interface = list_interface
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index < self.__list_interface.size():
                result = self.__list_interface.get(self.__index)
                self.__index += 1
                return result
            raise StopIteration


class ListInterface:
    def __init__(self, _list=None):
        pass

    def __iter__(self):
        return ListIterableInterface(self)

    def is_empty(self):
        pass

    def __contains__(self, content):
        pass

    def __str__(self):
        return self.__class__.__name__

    def size(self):
        pass

    def add(self, content: object):
        pass

    def insert(self, index: int, content: object):
        pass

    def set(self, index: int, content: object):
        pass

    def replace(self, lambda_expression, index):
        pass

    def clear(self):
        pass

    def remove(self, content: object):
        pass

    def pop(self, index):
        pass

    def move(self, element_index, target_index):
        pass

    def insertion_sort(self, asc=True):
        pass

    def __reversed__(self):
        pass

    def get(self, index: int):
        pass

    def get_node(self, index: int):
        pass

    def sublist(self, start_index, end_index):
        pass

    def retain_all(self, collection):
        pass


class SimpleNode(NodeInterface):
    def __init__(self, content: object = None, next_node=None):
        super().__init__(content)
        self.next_node = next_node


class SimpleLinkedListIterable(ListIterableInterface):
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


#   TODO:   Inspiration for which methods are needed:
#           https://www.digitalocean.com/community/tutorials/java-list
#   TODO: Idea, instead of temp_node.next_node use recursion
class SimpleLinkedList(ListInterface):

    #   TODO:   Constructor

    def __init__(self, _list=None):
        self.first_node: SimpleNode = None
        if _list is not None:
            self.convert(_list)

    #   TODO:   Methods to move through the list (iterable)

    def __iter__(self):
        #   For looping through "for content in linkedlist" or checking for content "content in linkedlist"
        return SimpleLinkedListIterable(self)

    #   TODO:   Methods to check the list.

    def is_empty(self):
        #   Checking if the list is empty
        return self.first_node is None

    def __contains__(self, content):
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
        if not 0 <= index < self.size():
            raise IndexError()
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
        if not 0 <= index < self.size():
            raise IndexError()
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

    def replace(self, lambda_expression, index=None):
        if self.is_empty():
            return
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
        if not 0 <= index < self.size():
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
        return self.get_node(index).content

    def get_node(self, index: int):
        #   Returns node at given index.
        #   Not visible outside SimpleLinkedList-class.
        if self.size() == 0 or not 0 <= index < self.size():
            raise IndexError()
        counter = 0
        temp_node = self.first_node
        while counter < index:
            temp_node = temp_node.next_node
            counter += 1
        return temp_node

    def convert(self, _list):
        self.clear()
        for element in _list:
            self.add(element)

    def sublist(self, start_index, end_index):
        #   Returns content between start_index (included) and end_index (excluded) as a SimpleLinkedList.
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


class DoubleNode(SimpleNode):
    def __init__(self, content: object = None, next_node=None, previous_node=None):
        super().__init__(content=content, next_node=next_node)
        self.previous_node = previous_node


class DoubleLinkedListIterable(SimpleLinkedListIterable):
    def __init__(self, double_linked_list):
        super().__init__(simple_linked_list=double_linked_list)

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
    def __init__(self, _list=None):
        super().__init__()
        self.last_node: DoubleNode = None
        if _list is not None:
            self.convert(_list)

    def __iter__(self):
        return DoubleLinkedListIterable(self)

    def is_empty(self):
        return super().is_empty() and self.last_node is None

    def __check_empty(self, func):
        def wrapper(func):
            if self.is_empty():
                return
            func()

        return wrapper

    def __check_empty_add_node(self, func, node):
        def wrapper(self, func, node):
            pass

    def __contains__(self, content):
        super().__contains__()

    def __str__(self):
        return super().__str__()

    def size(self):
        return super().size()

    def add(self, content: object):
        new_node = DoubleNode(content=content)
        if self.is_empty():
            self.first_node = new_node
            self.last_node = new_node
            return
        self.last_node.next_node = new_node
        new_node.previous_node = self.last_node
        self.last_node = new_node

    def insert(self, index: int, content: object):
        if not 0 <= index < self.size():
            raise IndexError()
        new_node = DoubleNode(content)
        if self.is_empty():
            self.first_node = new_node
            self.last_node = new_node
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node.previous_node = new_node
            self.first_node = new_node
            return
        # if index == self.size-1:
        counter = 1
        temp_node = self.first_node.next_node
        while counter < index and temp_node.next_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        temp_node.previous_node.next_node = new_node
        new_node.previous_node = temp_node.previous_node
        new_node.next_node = temp_node
        temp_node.previous_node = new_node

    def set(self, index: int, content: object):
        if not 0 <= index < self.size():
            raise IndexError()
        new_node = DoubleNode(content)
        if self.is_empty():
            self.first_node = new_node
            self.last_node = new_node
        if index == 0:
            new_node.next_node = self.first_node.next_node
            self.first_node
            return
        counter = 1
        temp_node = self.first_node.next_node
        while counter < index and temp_node.next_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        new_node.previous_node = temp_node.previous_node
        new_node.next_node = temp_node.next_node

    def replace(self, lambda_expression, index=None):
        super().replace(lambda_expression)

    def clear(self):
        super().clear()
        self.last_node = None

    def remove(self, content: object):
        if self.is_empty():
            return False
        temp_node = self.first_node
        if temp_node.content is content:
            self.first_node = temp_node.next_node
            self.first_node.previous_node = None
            return True
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node
            if temp_node.content is content:
                temp_node.previous_node.next_node = temp_node.next_node
                if temp_node.next_node is not None:
                    temp_node.next_node.previous_node = temp_node.previous_node
                else:
                    self.last_node = temp_node.previous_node
                return True
        return False

    def pop(self, index):
        if self.is_empty():
            return
        if not 0 <= index < self.size():
            raise IndexError()
        output = self.first_node.content
        if index == 0:
            self.first_node = self.first_node.next_node
            self.first_node.previous_node = None
            return output
        if index is self.size() - 1:
            output = self.last_node.content
            self.last_node = self.last_node.previous_node
            self.last_node.next_node = None
            return output
        counter = 1
        temp_node = self.first_node.next_node
        while temp_node.next_node is not None and counter < index - 1:
            counter += 1
            temp_node = temp_node.next_node
        output = temp_node.content
        temp_node.next_node.previous_node = temp_node.previous_node
        temp_node.previous_node.next_node = temp_node.next_node
        return output

    def move(self, element_index, target_index):
        super().move(element_index, target_index)

    # probably a better methode
    def insertion_sort(self, asc=True):
        super().insertion_sort()

    def __reversed__(self):
        #   Turns order of the list
        super().__reversed__()

    def get(self, index: int):
        return super().get(index)

    def get_node(self, index: int):
        return super().get_node(index)

    def convert(self, _list):
        super().convert(_list)

    def sublist(self, start_index, end_index):
        if start_index < 0 or end_index < start_index or self.size() < end_index:
            raise IndexError
        counter = 0
        temp_dll = DoubleLinkedList()
        temp_node = self.first_node
        while temp_node.next_node is not None and counter < end_index:
            if start_index <= counter:
                temp_dll.add(temp_node.content)
            temp_node = temp_node.next_node
            counter += 1
        if counter < end_index:
            temp_dll.add()

    def retain_all(self, collection):
        return super().retain_all(collection)


class ArrayNode:
    def __init__(self, content=None, _type=None):
        if type(content) is not _type:
            raise TypeError
        self.content = content


class ArrayListIterable:
    def __init__(self):
        pass


class ArrayList:
    def __init__(self, size: int = 25):
        self.values: Array = ()


def simple_linkedlist_example(amount: int = 1000):
    sl_list = SimpleLinkedList()
    for i in range(amount):
        sl_list.add(random.randint(-amount, amount))
    for i in range(sl_list.size()):
        print(sl_list.get(i))
    return sl_list


if __name__ == "__main__":
    node = ArrayNode()
    """arrl = (SimpleNode(), SimpleNode(), SimpleNode())
    print(arrl[0].content)
    arrl[0].content = 2
    print(arrl[0].content)"""
