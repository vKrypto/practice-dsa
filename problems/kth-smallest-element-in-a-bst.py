# coding: utf-8
"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
from . import  TreeNode
from typing import Optional


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder_traverse(node):
            if not node:
                return

            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        count = 1
        for value in inorder_traverse(root):
            if count == k:
                return value

            count += 1

    def in_order(self, root):
        if root is None:
            return
        if root.left:
            yield from self.in_order(root.left)
        if root.val is not None:
            yield root.val
        if root.right:
            yield from self.in_order(root.right)
            
    
    def kthSmallest_1(self, root: Optional[TreeNode], k: int) -> int:
        pre_order_list = self.in_order(root)
        for node_val in pre_order_list:
            k -= 1
            if k==0:
                return node_val