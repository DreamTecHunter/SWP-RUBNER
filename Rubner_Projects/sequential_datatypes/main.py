import random
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


def use_lists(length: int, random_range: int, *list_types):
    lists = []

    print("\nInit lists")
    for list_type in list_types:
        _list: ListInterface = list_type()
        lists.append(_list)
    for l in lists:
        print(l)

    print("\nCheck Emptiness")
    for l in lists:
        print(l.is_empty())

    print("\nAdd one element")
    for l in lists:
        l.add(144)
        print(l)

    print("\nCheck Emptiness Again")
    for l in lists:
        print(l.is_empty())

    print("\nAdd multiple random numbers")
    for l in lists:
        for i in range(length):
            l.add(random.randint(-random_range, random_range))
        print(l)

    print("\nCheck a random number, if it is in the list.")
    numb = random.randint(-random_range, random_range)
    print(f"looking for {numb}")
    for l in lists:
        print(f"{l}\t{l.__contains__(numb)}")

    print("\nSize")
    for l in lists:
        print(l.size())

    print("\nInsert")
    for l in lists:
        l.insert(0, 1000)
        print(l)

    print("\nSet")
    for l in lists:
        l.set(2, 2000)
        print(l)

    print("\nReplace")
    for l in lists:
        l.replace(lambda x: x * 2, 3)
        print(l)

    print("\nRemove")
    for l in lists:
        l.remove(5)
        print(l)

    print("\nPop")
    for l in lists:
        print(f"{l.pop(6)}\t{l}")

    print("\nReverse")
    for l in lists:
        # TODO: l.__reversed__()
        print(l)

    print("\nSort")
    for l in lists:
        l.sort()
        print(l)

    print("\nClear")
    for l in lists:
        l.clear()
        print(l)


if __name__ == '__main__':
    use_lists(20, 10, SimpleLinkedList, DoubleLinkedList, ArrayList)
