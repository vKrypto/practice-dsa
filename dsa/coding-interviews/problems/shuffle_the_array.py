# https://leetcode.com/problems/shuffle-the-array/


from typing import List

class Solution:
    # Runtime: 70 ms, faster than 82.00% of Python3 online submissions for Shuffle the Array.
    # Memory Usage: 14.1 MB, less than 90.23% of Python3 online submissions for Shuffle the Array.    
    # time complexity: o(n) and space complexity: o(len(nums))
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result += [nums[i], nums[i+n]]
        return result