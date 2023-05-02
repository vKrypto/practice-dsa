# https://leetcode.com/problems/diameter-of-binary-tree/

from . import TreeNode, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def diameterOfBinaryTree(node):
            if node is None:
                return 0
            
            left_dia = diameterOfBinaryTree(node.left)
            right_dia = diameterOfBinaryTree(node.right)

            diameter[0] = max(diameter[0], right_dia + left_dia)

            return 1+ max(right_dia , left_dia)
        
        diameterOfBinaryTree(root)
        return diameter[0]