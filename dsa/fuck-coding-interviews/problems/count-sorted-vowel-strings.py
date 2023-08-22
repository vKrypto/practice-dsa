# https://leetcode.com/problems/count-sorted-vowel-strings/submissions/


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5

        cache = {(1,0):5}
        def rec(n, last_char=0):
            # add-caching
            if (n, last_char) in cache:
                return cache[(n, last_char)]
            # base-case.
            if n == 1:
                return 5 - last_char + 1
            
            # index-case
            res_count = 0
            for i in [1, 2, 3, 4, 5]:
                if last_char <= i:
                    res_count += rec(n-1, last_char=i)
            cache[(n,last_char)] = res_count
            return res_count
            
        x = rec(n)
        return x


    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
            
        dp = [[None]*6 for _ in range(n+1)]
        def rec(n, last_char=0):
            # add-caching
            if dp[n][last_char] is not None:
                return dp[n][last_char]
            # base-case.
            if n == 1:
                return 5 - last_char + 1
            
            # index-case
            res_count = 0
            for i in [1, 2, 3, 4, 5]:
                if last_char <= i:
                    res_count += rec(n-1, last_char=i)
            dp[n][last_char] = res_count
            return res_count
            
        x = rec(n)
        return x
