# https://leetcode.com/problems/minimum-absolute-difference-in-bst/submissions/941812092/
from . import  TreeNode
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        vals = []

        def in_order(node):
            if node:
                in_order(node.left)
                vals.append(node.val)
                in_order(node.right)
                
        in_order(root)
        min_diff = float('infinity')
        for i in range(len(vals)-1):
            first, second = vals[i] , vals[i+1]
            min_diff = min(min_diff, vals[i+1] - vals[i])

        return min_diff