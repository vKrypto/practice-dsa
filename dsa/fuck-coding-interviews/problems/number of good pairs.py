# https://leetcode.com/problems/number-of-good-pairs/
from typing import List

class Solution:
    # 6 minutes..
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result  = 0
        for k1, v1 in enumerate(nums):
            for k2, v2 in enumerate(nums[k1+1:]):
                if v1 == v2:
                    result += 1
        return result
    
    # 8 minutes.
    # Runtime: 32 ms, faster than 96.26% of Python3 online submissions for Number of Good Pairs.
    # Memory Usage: 13.8 MB, less than 56.59% of Python3 online submissions for Number of Good Pairs.
    # time Complexity: O(2n) and space Complexity: O(n)
    def numIdenticalPairs_1(self, nums: List[int]) -> int:
        # group numbers
        group = {}
        for i in nums:
            if i in group:
                group[i] +=1
            else:
                group[i] = 1
        # iterate group
        result = 0
        for k, v in group.items():
            result += v*(v-1)/2
        return int(result)