# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        time complexity: o(n)
        space complexity: too much
        Runtime: 130 ms, faster than 57.48% of Python3 online submissions for Trapping Rain Water.
        Memory Usage: 16 MB, less than 9.86% of Python3 online submissions for Trapping Rain Water.
        """
        left_max = []
        temp = 0
        for i in height:
            left_max.append(temp)
            temp = max(temp, i)
        
        right_max = []
        temp = 0
        for i in height[::-1]:
            right_max.append(temp)
            temp = max(temp, i)
        right_max = right_max[::-1]
        
        total = 0
        n = len(height)
        for i in range(1, n-1):
            height_level = min(left_max[i], right_max[i])
            total += max(height_level - height[i], 0)
        return total
    
    def trap_2(self, height: List[int]) -> int:
        # get max_from_left, max_from_left
        max_from_left = [0] * len(height)
        max_yet = 0
        for i in range(len(height)):
            if height[i] > max_yet:
                max_yet = height[i]
            max_from_left[i] = max_yet 

        max_from_right = [0] * len(height)
        max_yet = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > max_yet:
                max_yet = height[i]
            max_from_right[i] = max_yet

        # calculate water trapped = water_level - ground_level at each index
        res = 0
        for i in range(len(height)):
            water_level = min(max_from_right[i], max_from_left[i])
            res += water_level - height[i]

        return res
