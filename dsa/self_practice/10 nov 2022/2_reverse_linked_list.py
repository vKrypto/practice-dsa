# https://leetcode.com/problems/reverse-linked-list/submissions/# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 56 ms, faster than 66.01% of Python3 online submissions for Reverse Linked List.
    Memory Usage: 15.4 MB, less than 55.05% of Python3 online submissions for Reverse Linked List.
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head:
            # deattach cur_elem from head.
            temp = head
            head = head.next
            
            temp.next = new_head #  add into new list
            new_head = temp # modifify new header.. of new linked list.
        return new_head