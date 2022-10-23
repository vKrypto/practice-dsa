"""
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        runtime complexity: O(n)
        Runtime: 822 ms, faster than 71.21% of Python3 online submissions for Container With Most Water.
        Memory Usage: 27.5 MB, less than 58.19% of Python3 online submissions for Container With Most Water.
        """
        l, r = 0, len(height) -1
        area_max = 0
        while r-l >0:
            area_max = max(area_max, (r-l) * min(height[r], height[l]))
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r-1
        return area_max