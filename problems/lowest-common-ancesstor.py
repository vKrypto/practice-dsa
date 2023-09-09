# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def finAncesstor(self, root, target):
        """
        return traversal path for ancesstor in order for that target.
        """
        if root is None:
            return []
        
        ancess=[]
        if target < root.val:
            ancess += self.finAncesstor(root.left, target)
            # dig left
        elif target > root.val:
            ancess += self.finAncesstor(root.right, target)
            # dig right
        ancess.append(root.val)
        return ancess
    
    def get_lowest_common(self, l1, l2):
        len_1 = len(l1)
        len_2 = len(l2)
        temp = None
        for i in range(1, min(len_1, len_2)+1):
            if l1[-i] == l2[-i]:
                temp = l1[-i]
            else:
                break
        return temp
            
    
    def lowestCommonAncestor_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        anc_1 = self.finAncesstor(root, p.val)
        anc_2 = self.finAncesstor(root, q.val)
        print(self.get_lowest_common(anc_1, anc_2))
        return 
     
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'=None) -> 'TreeNode':
        """
        find p, q in tree, then recursively clombs up til parent is same.
        """
        # termination case 1
        if root is None:
            return
        # termination case 2
        print(root.val, p.val)
        if q is None and root.val ==  p.val:
            return root
        if root.val < p.val:
            p_exist = self.lowestCommonAncestor(root.right, p)
        else:
            p_exist = self.lowestCommonAncestor(root.left, p)
        
        if q:
            if root.val < q.val:
                q_exist = self.lowestCommonAncestor(root.right, q)
            else:
               q_exist = self.lowestCommonAncestor(root.left, q)

            if p_exist and q_exist:
                return root
        return p_exist
