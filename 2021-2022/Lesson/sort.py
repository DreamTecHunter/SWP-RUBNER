import copy


def twice(list):
    return copy.deepcopy(list)


def bubble_sort(list):
    list_new = twice(list)
    for i in range(len(list_new)):
        for j in range(len(list_new) - i - 1):
            if list_new[j] > list_new[j + 1]:
                print(j)
                print(i)
                temp = list_new[j]
                list_new[j] = list_new[j + 1]
                list_new[j + 1] = temp
    return list_new


def insertion_sort(list):
    list_new = twice(list)
    for i in range(len(list_new) - 1):
        temp_index = i + 1
        for j in range(i + 1):
            if list_new[j] > list_new[temp_index]:
                temp_index = j
                break
        k = i + 1
        while temp_index < k:
            temp = list_new[k]
            list_new[k] = list_new[k - 1]
            list_new[k - 1] = temp
            k = k - 1
    return list_new


def unstable_selection_sort(list):
    list_new = twice(list)
    for i in range(len(list_new)):
        temp_index = i
        j = i + 1
        while j < len(list_new):
            if list_new[temp_index] > list_new[j]:
                temp_index = j
            j = j + 1
        temp = list_new[temp_index]
        list_new[temp_index] = list_new[i]
        list_new[i] = temp
    return list_new


if __name__ == "__main__":
    mList = [2, 5, 8, 6, 4, 8, 9, 10]
    print(mList)
    s_bubble_list = bubble_sort(mList)
    # print(mList)
    s_insertion_list = insertion_sort(mList)
    # print(mList)
    s_selection_list = unstable_selection_sort(mList)
    print(s_bubble_list)
    print(s_insertion_list)
    print(s_selection_list)

"""
import array
arr = array.array("1", [2,4,3])
"""
