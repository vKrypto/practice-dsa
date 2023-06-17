# https://leetcode.com/problems/container-with-most-water/
from typing import List

class Solution:
    """
    time limit exceed
    """
    def maxArea_brute_force(self, height: List[int]) -> int:
        max_res = 0
        for i, x in enumerate(height):
            for j, y in enumerate(height):
                temp = abs(i-j) * min(x,y)
                max_res = max(max_res, temp)
        return max_res

    """
    time limit exceed
    """
    def maxArea_brute_force_optimized(self, height: List[int]) -> int:
        max_res = 0
        for i, x in enumerate(height):
            for j, y in enumerate(height[i+1:]):
                temp = abs(j+1)* min(x,y)
                max_res = max(max_res, temp)
        return max_res

"""
patterns:
    left , right( two-pointer)
    calculate area, main_tain max_area
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
    left, right = 0, len(height)-1
    res = 0
    while left < right:
        container_height = min(height[left], height[right])
        container_width = right - left
        area = container_width * container_height
        if res < area:
            res = area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return res

# this solution is 99.98% faster with 99% memory for leet_code
"""
f = open('user.out', 'w')
for height in map(loads, stdin):
    print(maxArea_two_pointer(height), file=f)
exit(0)
"""