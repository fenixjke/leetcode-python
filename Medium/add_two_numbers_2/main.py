# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from list_node import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remainder = 0
        root = next_node = ListNode()
        while l1 or l2 or remainder:
            l1val = l2val = 0
            if l1:
                l1val = l1.val
                l1 = l1.next
            if l2:
                l2val = l2.val
                l2 = l2.next
            remainder, new_val = divmod(l1val + l2val + remainder, 10)
            next_node.next = ListNode(new_val)
            next_node = next_node.next
        return root.next


