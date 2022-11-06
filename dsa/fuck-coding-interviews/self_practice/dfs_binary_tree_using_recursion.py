# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        vals = [root.val]
        vals += self.preorderTraversal(root.left)
        vals += self.preorderTraversal(root.right)
        return vals

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        vals = self.postorderTraversal(root.left)
        vals += self.postorderTraversal(root.right)
        vals += [root.val]
        return vals

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        vals = self.inorderTraversal(root.left)
        vals += [root.val]
        vals += self.inorderTraversal(root.right)
        return vals