# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/


class Solution:
    def __init__(self, *args, **kwargs):
        self.memoized_results = {}

    def _lcs(self, text1: str, text2: str, idx_1=0, idx_2=0) -> int:
        """
        using recursions is quite costly
        """
        key = (idx_1, idx_2)
        if key in self.memoized_results:
            return self.memoized_results[key]
        
        if idx_1 == len(text1) or idx_2 == len(text2):
            res_sum = 0
        elif text1[idx_1] == text2[idx_2]:
            res_sum = self._lcs(text1, text2, idx_1+1, idx_2 +1)
            res_sum += ord(text1[idx_1])
        else:
            res_sum_1 = self._lcs(text1, text2, idx_1+1, idx_2)
            res_sum_2 = self._lcs(text1, text2, idx_1, idx_2 +1)
            if res_sum_2 < res_sum_1: 
                res_sum = res_sum_1
            else:
                res_sum = res_sum_2
        self.memoized_results[key] = res_sum
        
        return self.memoized_results[key]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # s1 = [ord(i) for i in s1]
        # s2 = [ord(i) for i in s2]

        lcs_sum = self._lcs(s1, s2)
        res = 0
        for i in s1:
            res += ord(i)
        for i in s2:
            res += ord(i)
        
        return res - 2* lcs_sum


class Solution2:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)
        dp=[[0 for x in range(m+1)] for x in range(n+1)]
        for i in range(1,n+1):
            dp[i][0]=dp[i-1][0]+ord(s1[i-1])

        for i in range(1,m+1):
            dp[0][i]=dp[0][i-1]+ord(s2[i-1])
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))

        return dp[n][m] 