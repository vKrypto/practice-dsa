# https://leetcode.com/problems/sqrtx/

class Solution:
    """
    # using linear search
    # Runtime: 1914 ms, faster than 19.60% of Python3 online submissions for Sqrt(x).
    # Memory Usage: 13.8 MB, less than 56.61% of Python3 online submissions for Sqrt(x).
    """
    def mySqrt_1(self, x: int) -> int:
        i = 1
        while True:
            temp_sq = i * i
            if temp_sq > x:
                return i-1
            i += 1

   
    """
    # using binary search
    # Runtime: 48 ms, faster than 83.92%  of Python3 online submissions for Sqrt(x).
    # Memory Usage: 13.8 MB, less than 56.61% of Python3 online submissions for Sqrt(x).
    """
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 0, x
        while l + 1 < r:
            mid = (r+l)//2
            mul = mid*mid
            if mul > x:
                r = mid
            elif mul < x:
                l = mid
            else:
                return mid
        return l
            