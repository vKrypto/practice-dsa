# https://leetcode.com/problems/sqrtx/submissions/

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while True:
            temp_sq = i * i
            if temp_sq > x:
                return i-1
            i += 1