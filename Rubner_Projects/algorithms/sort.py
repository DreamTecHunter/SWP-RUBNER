#   Stability, inplace
import random


def bubblesort(collection, asc: bool = True):
    for i in range(len(collection)):
        for j in range(len(collection) - 1 - i):
            if collection[j + 1] < collection[j] if asc else collection[j + 1] > collection[j]:
                collection[j + 1], collection[j] = collection[j], collection[j + 1]
    return collection


# TODO: Finishing
def insertion_sort(collection, asc: bool = True):
    print(collection)
    for i in range(len(collection)):
        position = 0
        for j in range(i):
            if collection[j] < collection[i]:
                position = j
        for j in range(i - 1, position, -1):
            collection[j], collection[j + 1] = collection[j + 1], collection[j]
        print(collection)
    return collection


def unstable_selection_sort(collection, asc: bool = True):
    for i in range(len(collection)):
        position = i
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[position] if asc else collection[j] > collection[position]:
                position = j
        collection[position], collection[i] = collection[i], collection[position]
        la[position], la[i] = la[i], la[position]
    return collection


def stable_selection_sort(collection, asc: bool = True):
    for i in range(len(collection)):
        position = i
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[position] if asc else collection[j] > collection[position]:
                position = j
        for j in range(i, position, -1):
            collection[j], collection[j - 1] = collection[j - 1], collection[j]
            la[j], la[j - 1] = la[j - 1], la[j]
    return collection


def quick_sort(collection, asc: bool = True):
    return collection


def mergesort(collection, asc: bool = True):
    return collection


def heapsort(collection, asc: bool = True):
    return collection


def tree_sort(collection, asc: bool = True):
    return collection


if __name__ == "__main__":
    l = [random.randint(-100, 100) for i in range(10)]
    la = ["A", "A", "B", "B", "C", "C", "D", "D"]
    print(l)
    insertion_sort(l, True)
    print(l)
