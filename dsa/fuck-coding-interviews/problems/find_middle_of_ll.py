# https://leetcode.com/problems/middle-of-the-linked-list/description/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Runtime: 48 ms, faster than 64.53% of Python3 online submissions for Middle of the Linked List.
    Memory Usage: 13.9 MB, less than 11.58% of Python3 online submissions for Middle of the Linked List.
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
        