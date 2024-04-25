from single_linked_list import SingleLinkedList
import importlib
main = importlib.import_module('Medium.2_add_two_numbers.main')


def test_1():
    list1 = SingleLinkedList.create_from_array([2, 4, 3])
    list2 = SingleLinkedList.create_from_array([5, 6, 4])
    assert (
        SingleLinkedList.compare(
            main.Solution().addTwoNumbers(list1, list2),
            SingleLinkedList.create_from_array([7, 0, 8]))
    )


def test_2():
    list1 = SingleLinkedList.create_from_array([0])
    list2 = SingleLinkedList.create_from_array([0])
    assert (
        SingleLinkedList.compare(
            main.Solution().addTwoNumbers(list1, list2),
            SingleLinkedList.create_from_array([0]))
    )


def test_3():
    list1 = SingleLinkedList.create_from_array([9, 9, 9, 9, 9, 9, 9])
    list2 = SingleLinkedList.create_from_array([9, 9, 9, 9])
    assert (
        SingleLinkedList.compare(
            main.Solution().addTwoNumbers(list1, list2),
            SingleLinkedList.create_from_array([8, 9, 9, 9, 0, 0, 0, 1]))
    )


def test_4():
    list1 = SingleLinkedList.create_from_array([2, 4, 9])
    list2 = SingleLinkedList.create_from_array([5, 6, 4, 9])
    assert (
        SingleLinkedList.compare(
            main.Solution().addTwoNumbers(list1, list2),
            SingleLinkedList.create_from_array([7, 0, 4, 0, 1]))
    )






