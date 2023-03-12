from simple_linked_list import *


class DoubleNode(SimpleNode):
    def __init__(self, content: object = None, next_node=None, previous_node=None):
        super().__init__(content=content, next_node=next_node)
        self.previous_node = previous_node

    def __str__(self):
        return super().__str__() + f", previous_node: {self.previous_node is not None}"


class DoubleLinkedListIterable(SimpleLinkedListIterable):
    def __init__(self, double_linked_list):
        super().__init__(double_linked_list)

    def __iter__(self):
        return super().__iter__()

    def __previous__(self):
        if 0 < super().__index:
            result = super().__linked_list.get(super().__index)
            super().__index -= 1
            return result
        raise StopIteration


class DoubleLinkedList(SimpleLinkedList):
    def __init__(self, _list=None):
        self.last_node: DoubleNode = None
        super().__init__(_list)

    def __iter__(self):
        return DoubleLinkedListIterable(self)

    def is_empty(self):
        return super().is_empty() and self.last_node is None

    def __contains__(self, content):
        return super().__contains__(content)

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

    @ListInterface.check_index
    def insert(self, index: int, content: object):
        new_node = DoubleNode(content)
        if self.is_empty():
            self.first_node = new_node
            self.last_node = new_node
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node.previous_node = new_node
            self.first_node = new_node
            return
        counter = 1
        temp_node = self.first_node.next_node
        while counter < index and temp_node.next_node is not None:
            counter += 1
            temp_node = temp_node.next_node
        temp_node.previous_node.next_node = new_node
        new_node.previous_node = temp_node.previous_node
        new_node.next_node = temp_node
        temp_node.previous_node = new_node

    # TODO: Doesn't work properly
    @ListInterface.check_index
    def set(self, index: int, content: object):
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

    @ListInterface.check_index
    @ListInterface.check_empty
    def pop(self, index):
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

    # TODO: Sort-methode not working properly
    def sort(self, asc=True):
        # super().sort(asc)
        i = 0
        while i < self.size():
            element = self.pop(i)
            j = 0
            while ((self.get(j) <= element) if asc else (self.get(j) > element)) and j < i:
                j += 1
            self.insert(j, element)
            i += 1

    def __reversed__(self):
        super().__reversed__()

    def get(self, index: int):
        return super().get(index)

    def get_node(self, index: int):
        return super().get_node(index)

    def convert(self, _list):
        super().convert(_list)

    def sublist(self, start_index, end_index):
        super().sublist()

    def retain_all(self, collection):
        return super().retain_all(collection)


if __name__ == "__main__":
    test_iterable(DoubleLinkedList([1, 2]))
