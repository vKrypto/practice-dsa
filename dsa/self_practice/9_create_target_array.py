# https://leetcode.com/problems/create-target-array-in-the-given-order/submissions/
from typing import List

class Solution:
    # Runtime: 57 ms, faster than 40.01% of Python3 online submissions for Create Target Array in the Given Order.
    # Memory Usage: 13.8 MB, less than 60.73% of Python3 online submissions for Create Target Array in the Given Order.
    # time complexity: o(n) and space complexity: o(n)
    # fixme: WE can improve space Complexity to o(n) by using a linked list.
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for k, v in enumerate(index):
            res = res[:v] + [nums[k]] + res[v:]
        return res