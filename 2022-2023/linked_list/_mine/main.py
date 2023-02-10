import random

from sequential_datatype import SimpleLinkedList


def do_simple_linked_list():
    def fill_sll(lower_limit, upper_limit, length, *lists):
        for i in range(len(lists)):
            for y in range(length):
                lists[i].add(random.randint(lower_limit, upper_limit))
        return lists

    def print_all(*lists):
        [print(l.__str__()) for l in lists]

    def sorting_sll(*lists):
        for i in range(len(lists)):
            if i % 2 == 0:
                lists[i].insertion_sort(True)
            else:
                lists[i].insertion_sort(False)

    print("\n$\tInitiation")
    sll0 = SimpleLinkedList()
    sll1 = SimpleLinkedList()
    print_all(sll0, sll1)
    print("\n$\tFilling SimpleLinkedList-objects.")
    fill_sll(-100, 100, 20, sll0, sll1)
    print_all(sll0, sll1)
    print("\n$\tShowing the length of the first list.")
    print(sll0.size())
    print("\n$\tSorting lists (every second list is sorted in descending order).")
    sorting_sll(sll0, sll1)
    print_all(sll0, sll1)
    print("\n$\tCreating and filling 3th list.")
    sll2 = SimpleLinkedList()
    fill_sll(-50, 50, 10, sll2)
    print_all(sll2)
    print("\n$\tAdding two elements to the end of the 3th list.")
    print("\tEvery datatype is possible to, but some Methods might not work with other types then integer.")
    sll2.add("B")
    sll2.add("Hello")
    print_all(sll2)
    print("\n$\tRemoving the (first) \'B\'")
    sll2.remove('B')
    print_all(sll2)
    print("\n$\t")


if __name__ == '__main__':
    do_simple_linked_list()
