# https://leetcode.com/problems/sum-of-left-leaves/submissions/941805786/

from . import Optional, TreeNode



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if root:
            # for left node 
            if root.left and (root.left.left or root.left.right):
                self.sumOfLeftLeaves(root.left)
            elif root.left:
                self.result += root.left.val
            # for right node
            if root.right:
                self.sumOfLeftLeaves(root.right)

        return self.result