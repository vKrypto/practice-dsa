# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # using recursion
        new_head = ListNode(next=head)
        def func(node):
            if node is None or node.next is None:
                return
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
            func(node)

        func(new_head)
        return new_head.next

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # using iteration
        new_head = node = ListNode(next=head)
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return new_head.next