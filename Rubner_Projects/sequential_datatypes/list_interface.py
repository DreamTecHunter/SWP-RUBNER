import functools
import random


class NodeInterface:
    def __init__(self, content: object = None):
        self.content = content

    def __str__(self):
        return f"{self.__class__.__name__}:{self.content}"


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
        if _list is not None:
            self.convert(_list)

    def __iter__(self):
        return ListIterableInterface(self)

    def is_empty(self):
        return self.size() == 0

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
        self.insert(self.pop(element_index))

    def sort(self, asc=True):
        pass

    def __reversed__(self):
        pass

    def get(self, index: int):
        pass

    def get_node(self, index: int):
        pass

    def convert(self, _list):
        self.clear()
        for element in _list:
            self.add(element)

    def sublist(self, start_index, end_index):
        pass

    def retain_all(self, collection):
        pass

    def check_index(func):
        def wrapper(self, index, *args):
            if not 0 <= index < self.size():
                raise IndexError
            return func(self, index, *args)

        return wrapper

    def check_empty(func):
        @functools.wraps(func)
        def wrapper(self, *args):
            if self.is_empty():
                return
            return func(self, *args)

        return wrapper


def test_iterable(l: ListInterface, length: int = 250, rand_range: int = 1000):
    for i in range(length):
        l.add(random.randint(-rand_range / 2, rand_range / 2))
    print(l)
    l.sort()
    print(l)

