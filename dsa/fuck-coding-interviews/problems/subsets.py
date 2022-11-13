from itertools import combinations
from typing import List

class Solution:
    """
    Runtime: 60 ms, faster than 49.80% of Python3 online submissions for Subsets.
    Memory Usage: 14 MB, less than 82.42% of Python3 online submissions for Subsets.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            res += [list(x) for x in combinations(nums, i)]
        return res
            