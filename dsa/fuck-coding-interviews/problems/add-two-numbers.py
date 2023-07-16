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
            if not(l1 and l2):
                break
            # move linked list pointer by one step
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remainder and head:
            head.next = ListNode(remainder) 
        return res.next

    def addTwoNumbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Beats 99.33%of users with Python3
        Beats 99.79%of users with Python3
        """
        res = head = ListNode(0)  # Use dummy node as the head
        remainder = 0

        while l1 or l2 or remainder:
            # Calculate in-place digit sum
            node_total = remainder + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            remainder = node_total // 10

            # Add a digit (temp node) to head
            temp = ListNode(node_total % 10)
            head.next = temp
            head = temp
            
            # Move linked list pointers by one step
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next  # Return the list starting from the next node of the dummy head
