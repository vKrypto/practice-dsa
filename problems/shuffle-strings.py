# https://leetcode.com/problems/shuffle-string/

from typing import List


class Solution:
    # Runtime: 85 ms, faster than 56.48% of Python3 online submissions for Shuffle String.
    # Memory Usage: 13.9 MB, less than 61.75% of Python3 online submissions for Shuffle String.
    # time complexity: o(3n) and space complexity: o(4n)
    def restoreString_1(self, s: str, indices: List[int]) -> str:
        dp = {v:s[k] for k, v in enumerate(indices)}
        res=[]
        total_len = len(s)
        for i in range(total_len):
            res += [dp[i]]
        return "".join(res)
    
    #Runtime: 68 ms, faster than 79.98% of Python3 online submissions for Shuffle String.
    # Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions for Shuffle String.
    # time complexity: o(2n) and space complexity: o(n)
    def restoreString(self, s: str, indices: List[int]) -> str:
        total_len = len(s)
        res=[None]* total_len
        for k, v in enumerate(indices):
            res[v] = s[k]
        return "".join(res)

