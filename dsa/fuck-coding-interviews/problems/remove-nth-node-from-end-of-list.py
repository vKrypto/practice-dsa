# coding: utf-8
"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
from . import ListNode
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        array = []
        node = head
        while node:
            array.append(node)
            node = node.next

        removed_node = array[-n]

        # If a node has no previous, it means the node is the head
        try:
            previous_node = array[-(n + 1)]
        except IndexError:
            head = removed_node.next
        else:
            previous_node.next = removed_node.next

        return head


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Calculate the length of the LinkedList in a full while loop
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length <= 1:
            return None

        # Convert the negative index to the 0-based index
        deleted_index = length - n

        if deleted_index == 0:
            head = head.next
            return head

        # Start from the head, and find the previous node of the node we're going to delete
        index = 0
        node = head
        while node:
            if index == deleted_index - 1:
                previous_node = node
                deleted_node = node.next
                previous_node.next = deleted_node.next
                return head

            index += 1
            node = node.next

        return head



class Solution3:

    # @staticmethod
    # def sll_to_list(sll):
    #     data = []
    #     while sll:
    #         data.append(sll.val)
    #         sll= sll.next
    #     return data

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        step 1: two pointers to head, move second to nth node.
        step 2: move both pointers till second.next is None
        step 3: delete node pointed by first_pointer
        """ 
        # assert self.sll_to_list(head) == [1,2,3,4,5]
        # step 1:
        first_pointer = second_pointer = head
        for _ in range(n):
            second_pointer = second_pointer.next
        # assert (self.sll_to_list(first_pointer), self.sll_to_list(second_pointer)) == ([1,2,3,4,5], [3,4,5])

        # write base code: when remove first node
        if second_pointer is None:
            return head.next

        # step 2:
        while second_pointer.next:
            second_pointer = second_pointer.next
            first_pointer = first_pointer.next
        # assert (self.sll_to_list(first_pointer), self.sll_to_list(second_pointer)) == ([3,4,5], [5])
        
        # step 3:
        first_pointer.next = first_pointer.next.next 
        return head
