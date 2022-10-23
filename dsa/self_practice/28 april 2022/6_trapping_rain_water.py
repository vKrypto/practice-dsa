# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        time compexity: o(n)
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
        for i in range(n):
            if i > 0 and i < n-1 :
                height_level = min(left_max[i], right_max[i])
                total += max(height_level - height[i], 0)
        return total