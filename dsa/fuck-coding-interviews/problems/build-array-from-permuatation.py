# https://leetcode.com/problems/build-array-from-permutation/
from typing import List

class Solution:
    # time complexity : O(n) and space complexity : O(n)
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
        