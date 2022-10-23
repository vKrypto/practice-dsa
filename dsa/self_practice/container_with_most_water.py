# https://leetcode.com/problems/container-with-most-water/

class Solution:
    """
    time limit exceed
    """
    def maxArea_bruteforce(self, height: List[int]) -> int:
        max_res = 0
        for i, x in enumerate(height):
            for j, y in enumerate(height):
                temp = abs(i-j) * min(x,y)
                max_res = max(max_res, temp)
        return max_res

    """
    time limit exceed
    """
    def maxArea_bruteforce_optimized(self, height: List[int]) -> int:
        max_res = 0
        n = len(height)
        for i, x in enumerate(height):
            for j, y in enumerate(height[i+1:]):
                temp = abs(j+1)* min(x,y)
                max_res = max(max_res, temp)
        return max_res

    """
    patterns:
        left , right( two-pointer)
        calcualte area, main_tain max_area
        if left < right:
            decrement left pointer
        else:
            decrement right pointer
    time complexity: o(n)
    space complexity: o(1)
    Runtime: 1111 ms, faster than 64.03% of Python3 online submissions for Container With Most Water.
    Memory Usage: 27.4 MB, less than 44.12% of Python3 online submissions for Container With Most Water.
    """
    def maxArea_two_pointer(self, height: List[int]) -> int:
        max_res = 0
        n = len(height)
        l, r= 0, n-1
        while l < r:
            max_res = max(max_res, (r-l)*min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_res