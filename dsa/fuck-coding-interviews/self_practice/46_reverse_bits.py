# https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits_1(self, n):
        num_bits = 0
        num_bin = ""
        for i in bin(n)[2:][::-1]:
            num_bin += i
            num_bits += 1
        
        bits_missing = 32 - num_bits
        num_bin += '0' * bits_missing
        return int(num_bin, 2)
    """
    Runtime: 33 ms, faster than 94.64% of Python3 online submissions for Reverse Bits.
    Memory Usage: 13.9 MB, less than 49.90% of Python3 online submissions for Reverse Bits.
    """
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = (n>>i) & 1
            res = res | (bit << (31-i))
        return res