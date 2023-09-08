# https://leetcode.com/problems/binary-tree-right-side-view/submissions/
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using BFS solution
        # base-case:
        if not root:
            return []

        cur_level = [root]
        res = []
        while cur_level:
            next_level=[]
            node_val = None
            for node in cur_level:
                node_val = node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            res.append(node_val)
            cur_level = next_level

        return res
    
    def rightSideView_1(self, root: Optional[TreeNode]) -> List[int]:
        """
        using dfs and maintaining a list for level wise
        """
        level_wise_items = []

        def preOrder(node:Optional[TreeNode], level:int=0):
            if node:
                try:
                    level_wise_items[level] = node.val
                except:
                    level_wise_items.append(node.val)
                if node.left:
                    preOrder(node.left, level+1)
                if node.right:
                    preOrder(node.right, level+1)

        preOrder(root)
        return level_wise_items
