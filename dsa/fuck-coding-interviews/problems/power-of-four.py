# https://leetcode.com/problems/power-of-four/submissions/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n  >= 4:
            n = n/4        
        return n == 1

    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n == 1:
                break
            # check if last two digit or not 0
            if n & 1 ==1 or n & 2 == 2 or n & 3 == 3:
                return False
            n = n >> 2
        return n > 0

    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n == 1:
                break
            # check if last two digit or not 0
            if n & 1 or (n >> 1)  & 1:
                return False
            n = n >> 2
        return n > 0

    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n.bit_count() ==1 and not(n & (n - 1)) and n & 1431655765 == n
