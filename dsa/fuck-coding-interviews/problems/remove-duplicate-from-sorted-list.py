# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    Runtime: 70 ms, faster than 62.11% of Python3 online submissions for Remove Duplicates from Sorted List.
    Memory Usage: 13.9 MB, less than 29.55% of Python3 online submissions for Remove Duplicates from Sorted List.
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        # use two pointers
        cur_node , old_node = head, None
        
        while cur_node:
            if old_node and old_node.val == cur_node.val:
                old_node.next = cur_node.next
            else:
                old_node = cur_node
            cur_node = cur_node.next
        return head
            
        