import random

from inspect import signature

from list_interface import ListInterface
from simple_linked_list import SimpleLinkedList
from double_linked_list import DoubleLinkedList
from array_list import ArrayList


def do(func, _list, start_message=None, message_before=None, message_after=None, end_message=None, **kwargs):
    for l in _list:
        print("\n" + l.__class__.__name__ + "." + func)
        if start_message is not None:
            print(start_message)
        print(l)
        if message_before is not None:
            print(message_before)
        value = getattr(l, func)(**kwargs) if len(signature(getattr(l, func)).parameters) != 0 else getattr(l, func)()
        if value is not None:
            print(value)
        if message_after is not None:
            print(message_after)
        print(l)
        if end_message is not None:
            print(end_message)


def use_lists(length: int = 100, random_range: int = 50, same_content=True, _exclude=None, _include=None, *list_types):
    if len(list_types) == 0:
        return
    parameter = {
        "index": random.randint(0, length - 1),
        "content": random.randint(-random_range, random_range),
        "lambda_expression": lambda x: x * 2,
        "collection": [i for i in range(-random_range, random_range, 2)],
        "start_index": 5 if 5 < length else 0,
        "end_index": 10 if 10 <= length else length - 1
    }
    # exclude check-methods because they return wrappers-functions/methods which alone won't work properly
    # convert-methods is used in constructor and in this function
    exclude = ["convert", "clear", "is_empty", "check_index", "check_empty", "move"]
    if _exclude is not None:
        exclude += _exclude
    include = ["__contains__", "__reversed__", "__len__"]
    if _include is not None:
        include += _include
    _list = []
    if same_content:
        _values: list = [random.randint(-random_range, random_range) for i in range(length)]
    for lt in list_types:
        _l: ListInterface = lt()
        if same_content:
            _l.convert(_list=_values)  # convert-methode
        else:
            for i in range(length):
                _l.add(random.randint(-random_range, random_range))
        _list.append(_l)
    li = ListInterface()
    function_names = [name for name in dir(li)
                      if callable(getattr(li, name)) and ((name[0:1] != "_" and name not in exclude) or name in include)
                      ]
    for fn in function_names:
        kwargs = {}
        for key in parameter:
            if key in signature(getattr(li, fn)).parameters.keys():
                kwargs[key] = parameter[key]
                if key == "index":
                    parameter[key] += 1
                    parameter[key] = parameter[key] % length
                if key == "content":
                    parameter[key] += 2 % 1000
        print("\n" + fn)
        do(fn, _list, **kwargs, message_before="arguments: " + str(kwargs))
        input()
        print("\n" + ("_" * 150) + "\n")


if __name__ == '__main__':
    print()
    use_lists(1000, 50, False, None, None, SimpleLinkedList, DoubleLinkedList, ArrayList)
