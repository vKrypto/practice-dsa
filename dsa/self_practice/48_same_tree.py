# Definition for a binary tree node.
from typing import Optional
from queue import Queue

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    """
    using simple recursion.
    """
    def isSameTree(self, p:Optional(TreeNode), q:Optional(TreeNode)) -> bool:
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # check value if any of is None
        if (p is None or q is None):
            if p is None and q is None:
                return True
            else:
                return False
            
        # check value
        if p.val != q.val:
            return False
        
        # check - recursion.
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        
        # looks good.
        return True

    
    def isSameTree(self, p:Optional(TreeNode), q:Optional(TreeNode)) -> bool:
        q = Queue()
