import time

from list_interface import ListInterface
from simple_linked_list import SimpleLinkedList
from double_linked_list import DoubleLinkedList
from array_list import ArrayList


def timer(func):
    def wrapper(*args):
        _time = time.perf_counter()
        output = func(*args)
        return output, time.perf_counter() - _time

    return wrapper


@timer
def do(name):
    print(name)
    return name


def stats(*args: ListInterface):
    for _list in args:
        pass


if __name__ == '__main__':
    output, time = do("Tobi")
    print(time)
    print("bye")
