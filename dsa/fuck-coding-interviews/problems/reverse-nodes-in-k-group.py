from . import ListNode, Optional

class Solution:

    def _reverse(self, orig_head):
        head = orig_head
        new_head = None  # this is where we build the reversed list (reusing the existing nodes)
        while head:
            temp = head  # temp is a reference to a node we're moving from one list to the other
            head = temp.next  # the first two assignments pop the node off the front of the list
            temp.next = new_head  # the next two make it the new head of the reversed list
            new_head = temp

        return [orig_head, new_head]

    # time == O(n), space == o(n/k)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur_head = cur_node = head
        list_group = []
        i = 1
        # step 1: split list into k-group
        while cur_node:
            if i%k == 0:
                next_cur_node = cur_node.next
                cur_node.next = None
                # store them with [tail, reverse_order_linked_list]
                list_group.append(self._reverse(cur_head))
                cur_head = cur_node = next_cur_node 
            else:
                cur_node = cur_node.next
            i += 1

        # step 2: merge groups:
        merged_list = merged_list_head = ListNode()
        for [tail, head] in list_group:
            merged_list.next = head
            merged_list = tail

        #ste p 3: add ungrouped part in merge list
        merged_list.next = cur_head

        return merged_list_head.next