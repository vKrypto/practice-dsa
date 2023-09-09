# coding: utf-8
"""
https://leetcode.com/problems/balanced-binary-tree/
"""  
 
from . import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        tree = {'is_balanced': True}

        def height(node):
            if not node or not tree['is_balanced']:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)
            if abs(left_h - right_h) > 1:
                tree['is_balanced'] = False

            return 1 + max(left_h, right_h)

        height(root)
        return tree['is_balanced']
