from typing import List

# https://leetcode.com/problems/counting-bits/


# T:O(NlogN)
# S:O(N)

class Solution:
    # built ins
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n+1)]
    
    #DP way
    def countBits_1(self, n):
        dp = [0]*(n+1)
        offset = 0

        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp

    # Bit manipulation approach, worst than built in
    def countBits_2(self, n):
        ans = []
        for i in range(n+1):
            cur = 0
            while i:
                cur += i & 1
                i >>= 1
            ans.append(cur)
        return ans
0# T:O(N)
# S:O(N)