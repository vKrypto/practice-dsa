# https://leetcode.com/problems/number-of-1-bits/submissions/


class Solution:

    def hammingWeight(self, n: int) -> int:
        return n.bit_count()