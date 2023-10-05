# https://leetcode.com/problems/reorder-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:

    @staticmethod
    def split_list(head):
        """
        time: o(n/2), space: o(1)
        splits into two(first_half in reverse manner, second_half)
        """
        slow = fast = head
        reverse = None
        
        count = 1
        while fast:
            last_slow = slow
            slow = slow.next

            if fast.next:
                fast = fast.next.next
                count += 2
            else:
                count += 1
                fast = None
            
            last_slow.next, reverse = reverse, last_slow

        # patch for even/odd inputs
        if count % 2:
            reverse, slow = slow, reverse
        return reverse, slow


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        time: o(n), space= O(1)
        """
        first, second = self.split_list(head)

        # merge both linked lists
        res = None
        while first or second:
            if first:
                first.next, res, first = res, first, first.next
            if second:
                second.next, res, second = res, second, second.next
        

class Solution2:
    # @staticmethod
    # def print_sll(sll):
    #     data = []
    #     while sll:
    #         data.append(sll.val)
    #         sll = sll.next
    #     return data 

    def reverse(self, sll):
        # input = [5, 6, 7], output [7, 6, 5]
        current = sll
        prev = None
        while(current is not None):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        time: o(3n/2), space: o(1)
        Do not return anything, modify head in-place instead.
        step 1: find middle node using hair and tortoise.
        step 2: split second half and reverse the sll.
        step 3: start merging first half and second half alternately.
        """
        # base case:
        if not(head.next and head.next.next):
            return
        # input sll = [1, 2, 3, 4, 5, 6, 7]
        first_pointer = second_pointer = temp = head.next
        # step 1:
        temp = first_pointer
        last_first_pointer = None
        while temp and temp.next:
            temp = temp.next.next
            last_first_pointer = second_pointer 
            second_pointer = second_pointer.next

        
        # assert (first_pointer.val, second_pointer.val) == (2, 5)
        # assert (self.print_sll(first_pointer), self.print_sll(second_pointer)) == ([2, 3, 4, 5, 6,7], [5, 6, 7])

        # step 2:
        last_first_pointer.next = None # splitting
        second_pointer = self.reverse(second_pointer)
        # 
        # assert (self.print_sll(head), self.print_sll(second_pointer)) ==([1, 2, 3, 4], [7, 6, 5])

        # step 3:
        current_node = head
        while second_pointer:
            second_node = second_pointer
            second_pointer = second_pointer.next
            current_node.next, second_node.next = second_node, current_node.next
            current_node = current_node.next.next 
        # print(self.print_sll(head))
