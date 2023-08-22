# https://leetcode.com/problems/get-maximum-in-generated-array/submissions/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = {0:0, 1:1}
        if n in dp:
            return dp[n]
        max_num = 0

        for i in range(2, n+1):
            if i%2==0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2 + 1]
            max_num = max(max_num, dp[i])

        return max_num