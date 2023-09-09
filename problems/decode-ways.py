# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings_rec(self, s: str) -> int:
        memo = {}
        len_s = len(s)

        def dfs(i=0):
            # use cache.
            if i in memo:
                return memo[i]
            # base-case 1: invalid route.
            if i > len_s -1:
                return 1
            if  not(i < len_s and s[i] != "0"):
                return 0
            
            res = dfs(i+1)
            if i+1 < len_s and int(s[i] + s[i+1]) <= 26:
                res += dfs(i+2)

            memo[i] = res
            return res
        
        return dfs()

    def numDecodings_iter_bottom_up(self, s: str) -> int:
        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]
