# https://leetcode.com/problems/edit-distance/description/

class Solution:
    # recursive cached solution, TLE
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        # base-case
        if not(n1 and n2):
            return n1 or n2


        cache =  {}
        def rec(i=0, j=0):
            if i >= n1:
                return max(n2 - j, 0)
            if j >= n2:
                return max(n1 - i, 0)
            if (i,j) in cache:
                return cache[(i,j)]

            res =  rec(i+1, j+1)
            if word1[i] != word2[j]:
                case_1 = 1 + rec(i, j+1) # insert into word1 from word2
                case_2 = 1 + rec(i+1, j) # delete a char from word 1
                return min(1 + res , case_1, case_2)
            cache[(i,j)] = res
            return res

        return rec()

    # Tabular solutions
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]
