from list_node import ListNode


class SingleLinkedList(object):
    @staticmethod
    def create_from_array(array):
        result = None
        for val in reversed(array):
            result = ListNode(val, result)
        return result

    @staticmethod
    def compare(list1, list2):
        result = (
                list1.val == list2.val and
                list1.next is None and list2.next is None or
                list1.next is not None and list2.next is not None
        )
        if not result:
            return result

        if list1.next is not None and list2.next is not None:
            result = SingleLinkedList.compare(list1.next, list2.next)

        return result
