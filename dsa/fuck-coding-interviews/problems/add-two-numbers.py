"""
https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 64 ms, faster than 96.83% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 13.9 MB, less than 88.18% of Python3 online submissions for Add Two Numbers.
        """  # noqa: E501
        res = head = ListNode()
        remainder = 0
        while l1 or l2:
            # calculate in-place digit sum
            node_total = remainder
            node_total += l1.val if l1 else 0
            node_total += l2.val if l2 else 0
            num, remainder = node_total%10, node_total//10
            
            # add a digit (temp node) to head
            temp = ListNode(num)
            head.next = temp
            head = temp
                
            # move linked list pointer by one step
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remainder and head:
            head.next = ListNode(remainder) 
        return res.next