# https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    """
    Runtime: 22 ms, faster than 99.66% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 13.8 MB, less than 95.90% of Python3 online submissions for Climbing Stairs.
    """
    def climbStairs(self, n: int) -> int:
        one = two = 1 
        for i in range(n-1):
            one, two = one+two, one
        return one