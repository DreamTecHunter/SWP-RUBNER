from list_interface import *


class ArrayNode(NodeInterface):
    def __init__(self, content=None):
        super().__init__(content)

    def __str__(self):
        return super().__str__()


class ArrayListIterable(ListIterableInterface):
    def __init__(self, array_list):
        super().__init__(array_list)

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        return super().__next__()


class ArrayList(ListInterface):
    __standard_initiation_size = 25

    def __init__(self, _type=int, size: int = __standard_initiation_size, _list=None):
        self.__initiation_size = size
        self.container = tuple(ArrayNode() for node in range(self.__initiation_size))
        self.__type = _type
        super().__init__(_list)

    def __iter__(self):
        return ListIterableInterface(self)

    def is_empty(self):
        return super().is_empty()

    def __contains__(self, content):
        for node in self.container:
            if content.__eq__(node.content):
                return True
        return False

    def __str__(self):
        return super().__str__() + \
            f"<{self.__type.__name__}>({self.size()}/{len(self.container)})" + \
            f":{[node.content for node in self.container if node.content is not None]}"

    def size(self):
        return sum(1 for node in self.container if node.content is not None)

    def __resize(self, multiplier=2):
        self.container = tuple(
            ArrayNode(self.container[i].content if i < self.size() else None) for i in range(
                len(self.container) * multiplier
            )
        )

    def add(self, content: object):
        if type(content) is not self.__type:
            raise TypeError()
        if self.size() == len(self.container):
            self.__resize()
        for node in self.container:
            if node.content is None:
                node.content = content
                return

    @ListInterface.check_index
    def insert(self, index: int, content: object):
        if type(content) is not self.__type:
            raise TypeError
        if self.size() == len(self.container):
            self.__resize()
        temp_content = content
        for i in range(index, self.size()):
            self.container[i].content, temp_content = temp_content, self.container[i].content
        self.add(temp_content)

    @ListInterface.check_index
    def set(self, index: int, content: object):
        self.container[index].content = content

    def replace(self, lambda_expression, index=None):
        if index is not None:
            if not 0 <= index < self.size():
                raise IndexError
        for node in self.container if index is None else [self.container[index]]:
            if node.content is not None:
                node.content = lambda_expression(node.content)

    def clear(self, resize=False):
        if resize:
            self.container = tuple(ArrayNode() for i in range(self.__initiation_size))
        else:
            for node in self.container:
                node.content = None

    def remove(self, content: object):
        if type(content) is not self.__type:
            raise TypeError
        start = False
        for i in range(self.size() - 1):
            if not start and content.__eq__(self.container[i].content):
                start = True
            if start:
                self.container[i].content = self.container[i + 1].content
        self.container[self.size() - 1].content = None

    @ListInterface.check_index
    def pop(self, index):
        output = self.container[index].content
        for i in range(index, self.size() - 1):
            self.container[i].content = self.container[i + 1].content
        self.container[self.size() - 1].content = None
        return output

    def move(self, element_index, target_index):
        super().move(element_index, target_index)

    def sort(self, asc=True):
        for i in range(self.size()):
            for j in range(self.size() - i - 1):
                if (
                        (self.container[j + 1].content < self.container[j].content)
                        if asc else
                        (self.container[j + 1].content >= self.container[j].content)
                ):
                    self.container[j + 1].content, self.container[j].content = self.container[j].content, \
                        self.container[j + 1].content

    def __reversed__(self):
        for i in range(int(self.size() / 2)):
            self.container[i].content, self.container[self.size() - i - 1].content = self.container[
                self.size() - i - 1].content, self.container[i].content

    @ListInterface.check_index
    def get(self, index: int):
        return self.container[index].content

    @ListInterface.check_index
    def get_node(self, index: int):
        return self.container[index]

    def sublist(self, start_index, end_index):
        if start_index < 0 or end_index < start_index or self.size() <= end_index:
            raise IndexError
        temp_arrl = ArrayList(self.__type)
        for i in range(self.size()):
            if start_index <= i < end_index:
                temp_arrl.add(self.container[i].content)
        return temp_arrl

    def retain_all(self, collection):
        temp_arrl = ArrayList(self.__type)
        for i in range(self.size()):
            if self.container[i].content in collection:
                temp_arrl.add(self.container[i].content)
        return temp_arrl


if __name__ == "__main__":
    test_iterable(ArrayList(int, _list=[1, 2]))
