# https://leetcode.com/problems/validate-binary-search-tree/submissions/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # usinng in order dfs with recursion 
    def validate(self, node: Optional[TreeNode], min_val, max_val):
            if not (min_val < node.val < max_val):
                self.is_valid = False
                return

            if node.left:
                self.validate(node.left, min_val, node.val)
                
            if node.right:
                self.validate(node.right, node.val, max_val)
                
            return
           
    """
    time compexity: O(n)
    space Complexity: O(1)
    Runtime: 82 ms, faster than 43.85% of Python3 online submissions for Validate Binary Search Tree.
    Memory Usage: 16.5 MB, less than 80.50% of Python3 online submissions for Validate Binary Search Tree.
    """ 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        if root:
            self.validate(root, float('-infinity'), float('infinity'))
        return self.is_valid