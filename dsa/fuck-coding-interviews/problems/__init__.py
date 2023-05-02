<<<<<<< HEAD

class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other or other.val
    
=======
from typing import Optional, List



class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None) -> Optional(List):
        self.val = val
        self.left = left
        self.right = right
>>>>>>> 1c4c3aa21db1f55a18a5b624e5165ce2f1d600c3
