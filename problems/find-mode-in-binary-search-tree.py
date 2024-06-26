# coding: utf-8
"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""
from collections import Counter
from typing import List, Optional


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def inorder_traverse(node):
            if not node:
                return

            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        results = []
        max_count = 0
        counter = Counter(val for val in inorder_traverse(root))
        for key, count in counter.most_common():
            # Counter.most_common(1) would return only 1 item
            # even if there are more than 1 items which have the same count.
            if count >= max_count:
                results.append(key)
                max_count = count
            else:
                break

        return results

    def findMode_2(self, root: Optional[TreeNode]) -> List[int]:
        count_map = {}

        # create count map same like Counter() but for tree
        def travervse(node):
            if node:
                count_map[node.val] = count_map.get(node.val,0) +1
                travervse(node.left)
                travervse(node.right)
        
        travervse(root)

        # find mode  items from count_map
        max_count = 0
        mode_items = []
        for val, count in count_map.items():
            if count > max_count:
                mode_items = [val]
                max_count = count
            elif count == max_count:
                mode_items.append(val)

        return mode_items
