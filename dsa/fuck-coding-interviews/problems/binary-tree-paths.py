# https://leetcode.com/problems/binary-tree-paths/description/
from . import *

class Solution:
    def __init__(self):
        self.root_paths = []

    def binaryTreePaths(self, root: Optional[TreeNode], root_path=[]) -> List[str]:
        if root:
            if not(root.left or root.right):
                # leaf node
                self.root_paths.append("->".join(root_path + [str(root.val)]))
            if root.left:
                self.binaryTreePaths(root.left, root_path + [str(root.val)])
            if root.right:
                self.binaryTreePaths(root.right, root_path + [str(root.val)])
                
        return self.root_paths