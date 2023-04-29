# https://leetcode.com/problems/subtree-of-another-tree/submissions/941795949/
from . import Optional, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_symmetrical(self, root1, root2):
        if root1 is None or root2 is None:
            return root2 == root1
        
        if root1.val == root2.val:
            return self.is_symmetrical(root1.left, root2.left) and self.is_symmetrical(root1.right, root2.right) 
        return False
        


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val:
            if self.is_symmetrical(root, subRoot):
                return True
        if root.left:
            if self.isSubtree(root.left, subRoot):
                return True
        if root.right:
            if self.isSubtree(root.right, subRoot):
                return True
        return False
        