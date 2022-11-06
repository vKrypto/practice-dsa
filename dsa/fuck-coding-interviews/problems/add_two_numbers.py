# coding: utf-8
"""
https://leetcode.com/problems/add-two-numbers/
"""
from typing import Optional


class ListNode:  # pragma: no cover
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode()
        dummy_head_result_node = result_node

        carry = 0
        while l1 or l2:
            # the length of `l1` and `l2` might be different
            if l1:
                value1 = l1.val
                next1 = l1.next
            else:
                value1 = 0
                next1 = None
            if l2:
                value2 = l2.val
                next2 = l2.next
            else:
                value2 = 0
                next2 = None

            val = value1 + value2 + carry
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0

            # in the first loop, `result_node` is currently `dummy_head_result_node`
            next_result_node = ListNode(val)
            result_node.next = next_result_node

            # prepare for the next loop
            result_node = next_result_node
            l1 = next1
            l2 = next2

        if carry >= 1:
            result_node.next = ListNode(carry)

        return dummy_head_result_node.next

    def addTwoNumbers_1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 60 ms, faster than 99.24% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 13.9 MB, less than 86.23% of Python3 online submissions for Add Two Numbers.
        """
        carry = 0
        cur_node = None
        while l1 or l2 or carry:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            carry = temp//10
            temp_node = ListNode(temp%10)
            if cur_node:
                cur_node.next = temp_node
            else:
                head = temp_node
            cur_node = temp_node
        return head
