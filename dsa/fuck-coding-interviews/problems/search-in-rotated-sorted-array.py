# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target < nums[m]:
                r = m-1